############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(tidyr)
library(ggplot2)
library(directlabels)
library(dplyr)
library(RMySQL)
library(magrittr)
source("../app_themes.R")
source("../data_loading.R")

wordbank <- src_mysql(dbname="wordbank")

admin.table <- tbl(wordbank, "common_administration")
child.table <- tbl(wordbank, "common_child")
instruments.table <- tbl(wordbank, "common_instrumentsmap")
momed.table <- tbl(wordbank, "common_momed")

instrument.tables <- get.instrument.tables(wordbank, instruments.table)

admins <- get.administration.data(momed.table, child.table,
                                  instruments.table, admin.table) %>%
  gather(measure, vocab, comprehension, production)

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

## DEBUGGING
#input <- list(language = "Danish", form = "WS", measure = "production",
#              qsize = ".1")
#plot.attr <- function(input){plot.attr.fun(input$form, input$measure)}
  
############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output) {
  
  data <- reactive({filter(admins,
                           language == input$language,
                           form == input$form,
                           measure == input$measure)})
    
  plot.attr <- reactive({plot.attr.fun(input$form, input$measure)})
  
  output$plot <- renderPlot({
    
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0, 1.0, by=qs)
    
    p.data <- data() %>%
      group_by(age) %>%
      mutate(percentile = rank(vocab)/length(vocab),
             quantile = cut(percentile, breaks=cuts, 
                            labels=cuts[2:length(cuts)]-qs/2))
        
    ggplot(p.data, aes(x=age, y=vocab, colour=quantile)) + 
      geom_jitter(width=.1) +
      geom_smooth(se=FALSE, span=1) +
      scale_x_continuous(name = "Age (months)",
                         breaks = plot.attr()$xbreaks,
                         limits = plot.attr()$xlims) +
      ylab(plot.attr()$ylabel) +
      scale_colour_discrete(name="Quantile Midpoint")
    
  })
  
  ### FIELD SELECTORS
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"), 
                   choices = unique(instrument.tables$language), selected = 1)
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"), 
                   choices = unique(filter(instrument.tables,
                                           language == input$language)$form), selected = 1)
  })
  
  output$measure_selector <- renderUI({
    if (input$form == "WG") {
      measures <- list("Produces" = "production", "Understands" = "comprehension")
    } else if (input$form == "WS") {
      measures <- list("Produces" = "production")
    }
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures, selected = 1)
  })
  
})
