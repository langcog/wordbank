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

admins <- get.administration.data(momed.table, child.table,
                                  instruments.table, admin.table) %>%
  gather(measure, vocab, comprehension, production)


## DEBUGGING
input <- list(language = "Danish", form = "WS", measure = "production",
              qsize = ".1")

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output) {
  
  output$plot <- renderPlot({
    
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0, 1.0, by=qs)
    
    data <- admins %>%
      filter(language == input$language,
             form == input$form,
             measure == input$measure) %>%
      group_by(age) %>%
      mutate(p = rank(vocab)/length(vocab),
             q = cut(p, breaks=cuts, 
                     labels=cuts[2:length(cuts)]-qs/2))
    
    if(input$form == "WG") {
      if(input$measure == "comprehension") {
        label <- "Size of Receptive Vocabulary"
      } else {
        label <- "Size of Productive Vocabulary" 
      }
      data %<>% filter(age >= 8 & age <= 18)
      xlims = c(8,18)
      xbreaks = 8:18
    } else {
      data %<>% filter(age >= 16 & age <= 30)
      xlims = c(16,30)
      xbreaks = 16:30
      label = "Size of Productive Vocabulary"
    }
    
    ggplot(data, aes(x=age, y=vocab, colour=q)) + 
      geom_jitter(width=.1) +
      geom_smooth(se=FALSE, span=1) +
      scale_x_continuous(name = "Age (months)",
                         breaks = xbreaks,
                         limits = xlims) +
      ylab(label) +
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
