library(shiny)
library(RMySQL)
library(dplyr)
library(magrittr)
source("../data_loading.R")

## DEBUGGING
input <- list(language = "English", form = "WS", age = c(18,30))

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
  wordbank <- connect.to.wordbank("local")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables) %>%
    select(data_id, language, form, age, sex, momed.level, comprehension, production) %>%
    rename(momed = momed.level) %>%
    mutate(sex = factor(sex, levels=c("F", "M", "O"), labels=c("Female", "Male", "Other")))
  
  items <- get.item.data(common.tables) %>%
    select(item.id, type, category, definition, language, form) %>%
    mutate(item.id = as.numeric(substr(item.id, 6, nchar(item.id))))
  
  instrument.tables <- get.instrument.tables(wordbank, common.tables)
  languages <- sort(unique(instrument.tables$language))
  #forms <- unique(instrument.tables$form)
  
  start.language <- function() {"English"}
  start.form <- function() {"WS"}
  
  
  input.language <- reactive({
    ifelse(is.null(input$language), start.language(), input$language)
  })
  
  input.form <- reactive({
    ifelse(is.null(input$form), start.form(), input$form)
  })
  
#  input.language <- reactive({input$language})
  
#  input.form <- reactive({input$form})
  
  instrument <- reactive({
    if(!is.null(input.language()) & !is.null(input.form())) {
      filter(instrument.tables,
             language == input.language(),
             form == input.form())
    }
  })
  
  data <- eventReactive(input$get_data, {
    
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
  
  output$table <- renderDataTable({
    data()
  }, options = list(orderClasses = TRUE))
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"),
                   choices = languages, selected = start.language())
  })
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(instrument.tables,
                                                   language == input.language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"),
                   choices = forms(), selected = start.form())
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
  
  output$loaded <- reactive({1})
  
})
