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

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "production",
#              qsize = ".2", age = 25)

shinyServer(function(input, output) {
  
  data <- reactive({filter(admins,
                           language == input$language,
                           form == input$form,
                           measure == input$measure,
                           age == input$age)})
  
  output$plot <- renderPlot({
    
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0, 1.0, by=qs)

    quantile.data <- data() %>%
      group_by(age) %>%
      mutate(percentile = rank(vocab)/length(vocab),
             quantile = cut(percentile, breaks=cuts, 
                            labels=cuts[2:length(cuts)]-qs/2))
    
    ggplot(quantile.data, aes(x=vocab, fill=quantile)) + 
      geom_histogram(binwidth=25) +
      xlab("Vocabulary") +
      ylab("Number of Children") + 
      scale_fill_discrete(name="Quantile Midpoint")
    
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
