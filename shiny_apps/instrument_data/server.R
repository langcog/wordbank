library(shiny)
library(dplyr)
library(magrittr)
library(wordbankr)
library()

## DEBUGGING
input <- list(language = "English", form = "WS", age = c(18,30))

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive(0)
  outputOptions(output, 'loaded', suspendWhenHidden = FALSE)
  
  admins <- get_administration_data(mode = "local") %>%
    select(data_id, language, form, age, sex, momed, comprehension, production) %>%
    mutate(sex = factor(sex, levels = c("F", "M", "O"),
                        labels = c("Female", "Male", "Other")))
  
  items <- get_item_data() %>%
    select(num_item_id, item_id, type, category, definition, language, form)
  
  languages <- sort(unique(items$language))

  start_language <- function() "English"
  start_form <- function() "WS"
  
  
  input_language <- reactive({
    ifelse(is.null(input$language), start_language(), input$language)
  })
  
  input_form <- reactive({
    ifelse(is.null(input$form), start_form(), input$form)
  })
  
  data <- eventReactive(input$get_data, {
    
    if(!is.null(input_language()) & !is.null(input_form())) {
      
      instrument_items <- items %>%
        filter(language == input_language(), form == input_form()) %>%
        select(-language, -form)
      
      get_instrument_data(input_language(), input_form(), items = NULL,
                          iteminfo = instrument_items,
                          administrations = select(admins, -language, -form, -comprehension, -production)) %>%
        select(-num_item_id) %>%
        arrange(data_id)
    }
  })
  
  output$table <- renderDataTable({
    data()
  }, options = list(orderClasses = TRUE))
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"),
                   choices = languages, selected = start_language())
  })
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(items,
                                                   language == input_language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"),
                   choices = forms(), selected = start_form())
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
