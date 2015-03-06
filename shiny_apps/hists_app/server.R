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

measure.fun <- function(input.form) {
  if (input.form == "WG") {
    measures <- list("Produces" = "production", "Understands" = "comprehension")
  } else if (input.form == "WS") {
    measures <- list("Produces" = "production")
  }
  return(measures)
}

min.age.fun <- function(form) {
  if (form == "WS") {
    return(18)
  } else if (form == "WG") {
    return(8)
  }
}

max.age.fun <- function(form) {
  if (form == "WS") {
    return(30)
  } else if (form == "WG") {
    return(16)
  }
}

binwidth.fun <- function(form) {
  if (form == "WS") {
    return(25)
  } else if (form == "WG") {
    return(10)
  }  
}

start.language <- function(language) {
  ifelse(is.null(language), "English", language)
}

start.form <- function(form) {
  ifelse(is.null(form), "WS", form)
}

start.measure <- function(measure) {
  ifelse(is.null(measure), "production", measure)
}

start.age <- function(age) {
  ifelse(is.null(age), 24, age)  
}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "production",
#              qsize = ".2", age = 25)

shinyServer(function(input, output, session) {
  
  forms <- reactive({unique(filter(instrument.tables,
                                   language == start.language(input$language))$form)})
  measures <- reactive({measure.fun(start.form(input$form))})
  min.age <- reactive({min.age.fun(start.form(input$form))})
  max.age <- reactive({max.age.fun(start.form(input$form))})
  
  data <- reactive({
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0, 1.0, by=qs)
    admins %>% filter(language == start.language(input$language),
                      form == start.form(input$form),
                      measure == start.measure(input$measure),
                      age == start.age(input$age)) %>%
    group_by(age) %>%
    mutate(percentile = rank(vocab)/length(vocab),
           quantile = cut(percentile, breaks=cuts, 
                          labels=cuts[2:length(cuts)]-qs/2))
  })
  
  binwidth <- reactive({binwidth.fun(start.form(input$form))})
  
  plot <- function() {
    ggplot(data(), aes(x=vocab, fill=quantile)) + 
      geom_histogram(binwidth=binwidth()) +
      xlab("\nVocabulary Size") +
      ylab("Number of Children\n") + 
      scale_fill_brewer(name="Quantile\nMidpoint",
                        palette=seq.palette)
  }
  
  output$plot <- renderPlot({
    plot()    
  }, height = function() {
    session$clientData$output_plot_width * 0.7
  })
  
  ### FIELD SELECTORS
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"), 
                   choices = languages, selected = start.language(NULL))
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"), 
                   choices = forms(), selected = start.form(NULL))
  })
  
  output$measure_selector <- renderUI({
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures(), selected = start.measure(NULL))
  })
  
  output$age_selector <- renderUI({
    sliderInput("age", label = h4("Age (Months)"), 
                min = min.age(), max = max.age(), value = (min.age()+max.age())/2)
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_distribution.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_distribution.pdf' },
    content = function(file) {
      pdf(file, width=10, height=7)
      print(plot())
      dev.off()
    })
  
})
