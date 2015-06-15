library(shiny)
library(RMySQL)
library(dplyr)
library(magrittr)
library(DT)
source("../data_loading.R")

## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "produces", age = c(16, 30))

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden = FALSE)
  
  wordbank <- connect.to.wordbank("local")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables) %>%
    select(data_id, language, form, age, sex, momed.level, comprehension, production) %>%
    rename(momed = momed.level) %>%
    mutate(sex = factor(sex, levels = c("F", "M", "O"), labels = c("Female", "Male", "Other")))
  
  items <- get.item.data(common.tables) %>%
    select(item.id, type, category, lexical_category, definition, language, form) %>%
    mutate(num.id = as.numeric(substr(item.id, 6, nchar(item.id))))
  
  instrument.tables <- init.instrument.tables(wordbank, common.tables)
  languages <- sort(unique(instrument.tables$language))
  
  start.language <- function() {"English"}
  start.form <- function() {"WS"}
  start.measure <- function() {"produces"}

  input.language <- reactive({
    ifelse(is.null(input$language), start.language(), input$language)
  })
  
  input.form <- reactive({
    ifelse(is.null(input$form), start.form(), input$form)
  })

  input.measure <- reactive({
    ifelse(is.null(input$measure), start.measure(), input$measure)
  })

  input.age_min <- reactive({
    if (is.null(input$age)) {
      age.min()
    } else {
      input$age[1]
    }
  })

  input.age_max <- reactive({
    if (is.null(input$age)) {
      age.max()
    } else {
      input$age[2]
    }
  })
  
  instrument <- reactive({
    inst <- filter(instrument.tables, language == input.language(),
                   form == input.form())$instrument_id
    for (inst_id in inst) {
      if (length(instrument.tables[instrument.tables$instrument_id == inst_id, ]$table[[1]]) == 0) {
        instrument.tables <<- add.instrument.table(wordbank, instrument.tables, inst_id)
      }
    }
    filter(instrument.tables, language == input.language(), form == input.form())
  })

  instrument_data <- reactive({
    
      instrument.items <- filter(items, language == input.language(), form == input.form(),
                                 type == "word") %>%
        select(-language, -form, -type)
      
      instrument.table <- instrument()$table[[1]]

      get.instrument.data(instrument.table, instrument.items$item.id) %>%
        rename(num.id = item.id) %>%
        mutate(produces = value == 'produces',
               understands = value == 'understands' | value == 'produces') %>%
        select(-value) %>%
        gather(measure, value, produces, understands) %>%
        left_join(select(admins, data_id, age)) %>%
        filter(!is.na(age)) %>%
        group_by(num.id, age, measure) %>%
        summarise(prop = round(mean(value, na.rm = TRUE), 2)) %>%
        left_join(instrument.items)
        
  })
      
  measure_data <- reactive({
    instrument_data() %>%
      filter(measure == input.measure()) %>%
      select(-measure)
  })
  
  data <- reactive({
    measure_data() %>%
      filter(age >= input.age_min(), age <= input.age_max()) %>%
      spread(age, prop) %>%
      ungroup() %>%
      select(-num.id, -item.id, -lexical_category)
  })
  
  output$table <- DT::renderDataTable({
    data()
  }, server = TRUE, filter = "top", style = "bootstrap", selection = "multiple",
  options = list(orderClasses = TRUE, processing = TRUE, pageLength = 25))
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"),
                   choices = languages, selected = input.language())
  })
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(instrument.tables,
                                                   language == input.language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"),
                   choices = forms(), selected = input.form())
  })
  
  measures <- reactive({
    if ("WG" == input.form()) {
      list("Produces" = "produces", "Understands" = "understands")
    } else {
      list("Produces" = "produces")
    } 
  })

  output$measure_selector <- renderUI({
    selectInput("measure", label = h4("Measure"), 
                choices = measures(), selected = input.measure())
  })

  age.min <- reactive({instrument()$age_min})
  age.max <- reactive({instrument()$age_max})

  output$age_selector <- renderUI({
    sliderInput("age", label = h4("Age (Months)"), 
                min = age.min(), max = age.max(), step = 1,
                value = c(age.min(), age.max()))
  })

  output$downloadAll = downloadHandler(
    'item_data.csv',
    content = function(file) {
      write.csv(data(), file)
  })

  output$downloadCurrent = downloadHandler(
    'item_data.csv',
    content = function(file) {
      s = as.numeric(input$table_rows_all)
      write.csv(data()[s, , drop = FALSE], file)
    })
  
  output$downloadSelected = downloadHandler(
    'item_data.csv',
    content = function(file) {
      s = as.numeric(input$table_rows_selected)
      write.csv(data()[s, , drop = FALSE], file)
    })
    
#   output$downloadData <- downloadHandler(
#     filename = function() { 'item_data.csv' },
#     content = function(file) {
#       write.csv(data(), file, row.names = FALSE)
#     })
  
  output$loading <- renderImage({
    return(list(
      src = "../images/loading.gif",
      contentType = "image/gif",
      alt = "Loading"
    ))
  }, deleteFile = FALSE)
  
  output$loaded <- reactive({1})
  
})
