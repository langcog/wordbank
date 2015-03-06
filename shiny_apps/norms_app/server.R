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

plot.attr.fun <- function(form, measure) {
  plot.attr = list()
  if(form == "WG") {
    if(measure == "comprehension") {
      plot.attr$ylabel <- "Size of Receptive Vocabulary"
    } else {
      plot.attr$ylabel <- "Size of Productive Vocabulary" 
    }
    plot.attr$xlims = c(8,18)
    plot.attr$xbreaks = 8:18
  } else {
    plot.attr$ylabel = "Size of Productive Vocabulary"
    plot.attr$xlims = c(16,30)
    plot.attr$xbreaks = 16:30
  }
  return(plot.attr)
}

measure.fun <- function(input.form) {
  if (input.form == "WG") {
    measures <- list("Produces" = "production", "Understands" = "comprehension")
  } else if (input.form == "WS") {
    measures <- list("Produces" = "production")
  }
  return(measures)
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

## DEBUGGING
#input <- list(language = "Danish", form = "WS", measure = "production",
#              qsize = ".1")
#plot.attr <- function(){plot.attr.fun(input$form, input$measure)}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output, session) {
  
  data <- reactive({
    qs = as.numeric(input$qsize)
    cuts = seq(0.0, 1.0, by=qs)
    admins %>% filter(language == start.language(input$language),
                      form == start.form(input$form),
                      measure == start.measure(input$measure)) %>%
      group_by(age) %>%
      mutate(percentile = rank(vocab) / length(vocab),
             quantile = cut(percentile,
                            breaks=cuts, 
                            labels=cuts[2:length(cuts)]-qs/2))
  })
  
  plot.attr <- reactive({plot.attr.fun(start.form(input$form),
                                       start.measure(input$measure))})
  
  plot <- function() {
    ggplot(data(), aes(x=age, y=vocab, colour=quantile)) + 
      geom_jitter(width=.1) +
      geom_smooth(method="loess", se=FALSE, size=1.5) +
      scale_x_continuous(name="\nAge (months)",
                         breaks=plot.attr()$xbreaks,
                         limits=plot.attr()$xlims) +
      ylab(paste(plot.attr()$ylabel, "\n", sep="")) +
      scale_colour_brewer(name="Quantile\nMidpoint",
                          palette=seq.palette) +
      theme(text=element_text(family=font))
  }
  
  forms <- reactive({unique(filter(instrument.tables,
                                   language == start.language(input$language))$form)})
  
  measures <- reactive({measure.fun(start.form(input$form))})
  
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
  
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_norms.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_norms.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
  # output$downloadReport <- downloadHandler(
  #   filename = function() { 'vocabulary_norms_report.pdf' },
  #   
  #   content = function(file) {
  #     library(rmarkdown)
  #     out <- render('report.Rmd', pdf_document())
  #     file.rename(out, file)
  #   })
  
})
