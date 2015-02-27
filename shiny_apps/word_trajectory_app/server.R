############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
rm(list=ls())
library(shiny)
library(tidyr)
library(ggplot2)
library(directlabels)
library(dplyr)
library(RMySQL)
library(magrittr)
source("../app_themes.R")
source("../data_loading.R")
#options(shiny.error=NULL)
Sys.setlocale(locale="C")

wordbank <- src_mysql(dbname="wordbank")

admin.table <- tbl(wordbank, "common_administration")
child.table <- tbl(wordbank, "common_child")
instruments.table <- tbl(wordbank, "common_instrumentsmap")
momed.table <- tbl(wordbank, "common_momed")
wordmapping.table <- tbl(wordbank, "common_wordmapping")

admins <- get.administration.data(momed.table, child.table, instruments.table, admin.table)
items <- get.item.data(wordmapping.table, instruments.table)

list.words.by.definition <- function(word.data) {
  words <- word.data$item.id
  names(words) <- word.data$definition
  return(words)
}

list.words.by.id <- function(word.data) {
  words <- word.data$definition
  names(words) <- word.data$item.id
  return(words)
}

tables <- get.instrument.tables(wordbank, instruments.table)
instrument.tables <- tables %>%
  group_by(instrument_id) %>%
  do(words.by.definition = list.words.by.definition(filter(items, instrument_id==.$instrument_id,
                                                           type=='word')),
     words.by.id = list.words.by.id(filter(items, instrument_id==.$instrument_id,
                                           type=='word'))) %>%
  left_join(tables)

## DEBUGGING
#input <- list(language = "Danish", form = "WS", measure = "produces",
#              word1 = "item_1", word2 = "item_1", word3 = "item_1")
# instrument <- function() {return(filter(instrument.tables,
#                                       language == input$language,
#                                       form == input$form))}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output) {  
  
  instrument <- reactive({filter(instrument.tables,
                                 language == input$language,
                                 form == input$form)})
  
  ### PLOT RENDERER
  output$plot <- renderPlot({
    
    instrument.table <- instrument()$table[[1]]
    instrument.words.by.definition <- instrument()$words.by.definition[[1]]
    instrument.words.by.id <- instrument()$words.by.id[[1]]
    
    data <- get.instrument.data(instrument.table, input$words) %>%
      filter(measure == input$measure) %>%
      left_join(admins) %>%
      group_by(item.id, age) %>%
      summarise(score = mean(value, na.rm=TRUE)) %>%
      rowwise %>%
      mutate(word = instrument.words.by.id[[paste("item_", item.id, sep="")]])
    
    if(input$form == "WG") {
      if(input$measure == "understands") {
        label <- "Proportion of Children Understanding"
      } else {
        label <- "Proportion of Children Producing" 
      }
      data %<>% filter(age >= 8 & age <= 18)
      xlims = c(8,20)
      xbreaks = 8:18
    } else {
      data %<>% filter(age >= 16 & age <= 30)
      xlims = c(16,32)
      xbreaks = 16:30
      label = "Proportion of Children Producing"
    }
    
    ggplot(data, aes(x=age, y=score, colour=word, label=word)) +
      geom_smooth(se=FALSE, method="loess") +
      geom_point() +
      scale_x_continuous(name = "Age (months)",
                         breaks = xbreaks,
                         limits = xlims) +
      scale_y_continuous(name = label,
                         limits = c(-.01,1),
                         breaks = seq(0,1,.25)) +
      theme(legend.position="none") +
      geom_dl(method = list(dl.trans(x=x +.2),"last.qp",cex=1)) +
      scale_colour_brewer(palette="Set1")
    
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
      measures <- list("Produces" = "produces", "Understands" = "understands")
    } else if (input$form == "WS") {
      measures <- list("Produces" = "produces")
    }
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures, selected = 1)
  })
  
  output$words_selector <- renderUI({
    selectizeInput("words", label = h4("Words"), 
                   choices = instrument()$words.by.definition[[1]],
                   selected = 1, multiple = TRUE)
  })
  
})
