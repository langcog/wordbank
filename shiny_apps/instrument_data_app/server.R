############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(RMySQL)
library(dplyr)
library(magrittr)
source("../data_loading.R")

wordbank <- src_mysql(dbname="wordbank")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables$momed,
                                  common.tables$child,
                                  common.tables$instrumentsmap,
                                  common.tables$administration) %>%
  select(data_id, language, form, age, sex, momed.level, comprehension, production) %>%
  rename(momed = momed.level)

items <- get.item.data(common.tables$wordmapping,
                       common.tables$instrumentsmap) %>%
  select(item.id, type, category, definition, language, form) %>%
  mutate(item.id = as.numeric(substr(item.id, 6, nchar(item.id))))

instrument.tables <- get.instrument.tables(wordbank, common.tables$instrumentsmap)
languages <- unique(instrument.tables$language)
forms <- unique(instrument.tables$form)

start.language <- function() {"English"}
start.form <- function() {"WS"}


## DEBUGGING
#input <- list(language = "English", form = "WS", age = c(18,30))

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output, session) {
  
  input.language <- reactive({
    input$language
    #    ifelse(is.null(input$language), start.language(), input$language)
  })
  
  input.form <- reactive({
    input$form
    #    ifelse(is.null(input$form), start.form(), input$form)
  })
  
  instrument <- reactive({
    if(!is.null(input.language()) & !is.null(input.form())) {
      filter(instrument.tables,
             language == input.language(),
             form == input.form())
    }
  })
  
  
  data <- reactive({
    
    if(!is.null(input.language()) & !is.null(input.form())) {
      
      instrument.items <- filter(items, language == input.language(), form == input.form()) %>%
        select(-language, -form)
      
      instrument.table <- instrument()$table[[1]]
      fields <- as.character(instrument.table$select[2:length(instrument.table$select)])
      
      get.instrument.data(instrument.table, fields) %>%
        left_join(instrument.items) %>%
        left_join(select(admins, -language, -form, -comprehension, -production)) %>%
        arrange(data_id)
    }
  })
  
  #  forms <- reactive({
  #    print(input.language())
  #    if(!is.null(input.language())) {
  #      unique(filter(instrument.tables, language == input.language())$form)
  #    } else {c()}
  #  })
  
  output$table <- renderDataTable({
    data()
  }, options = list(orderClasses = TRUE))
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"),
                   choices = languages)
    #                   selected = start.language())
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"),
                   choices = forms)
    #                   selected = start.form())
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'instrument_data.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$loading <- renderImage({
    return(list(
      src = "../images/loading.gif",
      contentType = "image/gif",
      alt = "Loading"
    ))
  }, deleteFile = FALSE)
  
})
