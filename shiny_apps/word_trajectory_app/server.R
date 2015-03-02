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
Sys.setlocale(locale="C")

wordbank <- src_mysql(dbname="wordbank")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables$momed.table,
                                  common.tables$child.table,
                                  common.tables$instruments.table,
                                  common.tables$admin.table)

items <- get.item.data(common.tables$wordmapping.table,
                       common.tables$instruments.table)

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

tables <- get.instrument.tables(wordbank, common.tables$instruments.table)
instrument.tables <- tables %>%
  group_by(instrument_id) %>%
  do(words.by.definition = list.words.by.definition(filter(items, instrument_id==.$instrument_id,
                                                           type=='word')),
     words.by.id = list.words.by.id(filter(items, instrument_id==.$instrument_id,
                                           type=='word'))) %>%
  left_join(tables)

languages <- unique(instrument.tables$language)

start.language <- function(language) {
  ifelse(is.null(language), "English", language)
}

start.form <- function(form) {
  ifelse(is.null(form), "WS", form)
}

start.measure <- function(measure) {
  ifelse(is.null(measure), "produces", measure)
}

start.words <- function(words) {
  if(is.null(words)) {c("item_1")} else {words}
  }


data.fun <- function(input.language, input.form, input.measure, input.words) {
  
  instrument <- filter(instrument.tables, language == input.language, form == input.form)
  instrument.table <- instrument$table[[1]]
  instrument.words.by.definition <- instrument$words.by.definition[[1]]
  instrument.words.by.id <- instrument$words.by.id[[1]]

  data <- get.instrument.data(instrument.table, input.words) %>%
    mutate(produces = value == 'produces',
           understands = value == 'understands' | value == 'produces') %>%
    select(-value) %>%
    gather(measure, value, produces, understands) %>%
    filter(measure == input.measure) %>%
    left_join(admins) %>%
    group_by(item.id, age) %>%
    summarise(score = mean(value, na.rm=TRUE)) %>%
    rowwise %>%
    mutate(word = instrument.words.by.id[[paste("item_", item.id, sep="")]])
    
  if (input.form == "WS") {
    data %<>% filter(age >= 16 & age <= 30)
  } else if (input.form == "WG") {
    data %<>% filter(age >= 8 & age <= 18)      
  }
  return(data)
  
}

plot.attr.fun <- function(input.form, input.measure) {
  plot.attr = list()
  if (input.form == "WG") {
    plot.attr$xlims = c(8,21)
    plot.attr$xbreaks = 8:18
    if (input.measure == "understands") {
      plot.attr$ylabel <- "Size of Receptive Vocabulary"
    } else if (input.measure == "produces") {
      plot.attr$ylabel <- "Size of Productive Vocabulary" 
    }
  } else if (input.form == "WS") {
    plot.attr$xlims = c(16,33)
    plot.attr$xbreaks = 16:30
    plot.attr$ylabel = "Size of Productive Vocabulary"
  }
  return(plot.attr)
}

measure.fun <- function(input.form) {
  if (input.form == "WG") {
    measures <- list("Produces" = "produces", "Understands" = "understands")
  } else if (input.form == "WS") {
    measures <- list("Produces" = "produces")
  }
  return(measures)
}

## DEBUGGING
#input <- list(language = "Danish", form = "WS", measure = "produces",
#              word1 = "item_1", word2 = "item_1", word3 = "item_1")
# instrument <- function() {return(filter(instrument.tables,
#                                       language == input$language,
#                                       form == input$form))}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output) {
  
  data <- reactive({data.fun(start.language(input$language),
                             start.form(input$form),
                             start.measure(input$measure),
                             start.words(input$words))})
  plot.attr <- reactive({plot.attr.fun(start.form(input$form),
                                       start.measure(input$measure))})
  words <- reactive({filter(instrument.tables,
                            language == start.language(input$language),
                            form == start.form(input$form))$words.by.definition[[1]]})
  forms <- reactive({unique(filter(instrument.tables,
                                   language == start.language(input$language))$form)})
  measures <- reactive({measure.fun(start.form(input$form))})
  
  ### PLOT RENDERER
  output$plot <- renderPlot({
    
    ggplot(data(), aes(x=age, y=score, colour=word, label=word)) +
      geom_smooth(se=FALSE, method="loess") +
      geom_point() +
      scale_x_continuous(name = "Age (months)",
                         breaks = plot.attr()$xbreaks,
                         limits = plot.attr()$xlims) +
      scale_y_continuous(name = plot.attr()$ylabel,
                         limits = c(-.01,1),
                         breaks = seq(0,1,.25)) +
      theme(legend.position="none") +
      geom_dl(method = list(dl.trans(x=x +.2),"last.qp",cex=1)) +
      scale_colour_brewer(palette="Set1")
    
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
  
  output$words_selector <- renderUI({
    selectizeInput("words", label = h4("Words"), 
                   choices = words(),
                   selected = start.words(NULL),
                   multiple = TRUE)
  })
  
})
