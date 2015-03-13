############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
source("../app_themes.R")
source("../data_loading.R")

wordbank <- src_mysql(dbname="wordbank")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables$momed,
                                  common.tables$child,
                                  common.tables$instrumentsmap,
                                  common.tables$administration) %>%
  gather(measure, vocab, comprehension, production)

instrument.tables <- get.instrument.tables(wordbank, common.tables$instrumentsmap)

languages <- unique(instrument.tables$language)

binwidth.fun <- function(form) {
  if (form == "WS") {
    return(25)
  } else if (form == "WG") {
    return(10)
  }  
}

start.language <- function() {"English"}
start.form <- function() {"WS"}
start.measure <- function() {"production"}

#start.age <- function(age) {
#  ifelse(is.null(age), 24, age)  
#}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "production",
#              qsize = ".2", age = 25)

shinyServer(function(input, output, session) {
  
  input.language <- reactive({ifelse(is.null(input$language),
                                     start.language(), input$language)})
  input.form <- reactive({ifelse(is.null(input$form),
                                 start.form(), input$form)})
  input.measure <- reactive({ifelse(is.null(input$measure),
                                    start.measure(), input$measure)})
  input.age <- reactive({input$age})
  
  instrument <- reactive({filter(instrument.tables,
                                 language == input.language(),
                                 form == input.form())})
  
  data <- reactive({
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0, 1.0, by=qs)
    admins %>% filter(language == input.language(),
                      form == input.form(),
                      measure == input.measure(),
                      age == input.age()) %>%
      group_by(age) %>%
      mutate(percentile = rank(vocab)/length(vocab),
             quantile = cut(percentile, breaks=cuts, 
                            labels=cuts[2:length(cuts)]-qs/2))
  })
  
  binwidth <- reactive({binwidth.fun(input.form())})
  
  plot <- function() {
    ggplot(data(), aes(x=vocab, fill=quantile)) + 
      geom_histogram(binwidth=binwidth()) +
      xlab("\nVocabulary Size") +
      ylab("Number of Children\n") + 
      scale_fill_brewer(name="Quantile\nMidpoint",
                        palette=seq.palette) +
      theme(text=element_text(family=font))
  }
  
  forms <- reactive({unique(filter(instrument.tables,
                                   language == input.language())$form)})
  
  measures <- reactive({
    if (input.form() == "WG") {
      list("Produces" = "production", "Understands" = "comprehension")
    } else if (input.form() == "WS") {
      list("Produces" = "production")
    }
  })
  
  output$plot <- renderPlot({
    plot()    
  }, height = function() {
    session$clientData$output_plot_width * 0.7
  })
  

  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"), 
                   choices = languages, selected = start.language())
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"), 
                   choices = forms(), selected = start.form())
  })
  
  output$measure_selector <- renderUI({
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures(), selected = start.measure())
  })
  
  age.min <- reactive({instrument()$age_min})
  age.max <- reactive({instrument()$age_max})
  
  output$age_selector <- renderUI({
    sliderInput("age", label = h4("Age (Months)"), 
                min = age.min(), max = age.max(), step = 1,
                value = floor((age.min()+age.max())/2))
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_distribution.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_distribution.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
})
