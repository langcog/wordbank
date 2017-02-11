library(shiny)
library(dplyr)
library(tidyr)
library(DT)
library(wordbankr)
mode <- "local"

input <- list(language = "English", form = "WS", measure = "produces",
              age = c(16, 30))

shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  instruments <- get_instruments(mode = mode)
  languages <- sort(unique(instruments$language))

  start_language <- "English"
  start_form <- "WS"
  start_measure <- "produces"

  input_language <- reactive({
    ifelse(is.null(input$language), start_language, input$language)
  })

  input_form <- reactive({
    ifelse(is.null(input$form), start_form, input$form)
  })

  input_measure <- reactive({
    ifelse(is.null(input$measure), start_measure, input$measure)
  })

  input_age_min <- reactive({
    if (is.null(input$age)) {
      age_min()
    } else {
      input$age[1]
    }
  })

  input_age_max <- reactive({
    if (is.null(input$age)) {
      age_max()
    } else {
      input$age[2]
    }
  })

  instrument <- reactive({
    filter(instruments, language == input_language(), form == input_form())
  })

  data <- reactive({
    get_instrument_data(input_language(), input_form(),
                        administrations = TRUE,
                        iteminfo = TRUE,
                        mode = mode) %>%
      mutate(produces = value == "produces",
             understands = value == "understands" | value == "produces") %>%
      select(-value) %>%
      gather(measure, value, produces, understands) %>%
      filter(measure == input_measure(),
             age >= input_age_min(), age <= input_age_max()) %>%
      group_by(num_item_id, definition, type, category, age) %>%
      summarise(prop = round(sum(value, na.rm = TRUE) / length(value), 2)) %>%
      spread(age, prop)
  })

  output$table <- renderDataTable(
    data(), server = TRUE, filter = "top", style = "bootstrap",
    rownames = FALSE, selection = "multiple",
    options = list(orderClasses = TRUE, processing = TRUE, pageLength = 25)
  )

  output$language_selector <- renderUI({
    selectizeInput("language", label = h4("Language"),
                   choices = languages, selected = input_language())
  })

  forms <- reactive({
    valid_form <- function(form) {
      form %in% unique(filter(instruments,
                              language == input_language())$form)
    }
    Filter(valid_form, list("Words & Sentences" = "WS",
                            "Words & Gestures" = "WG",
                            "Oxford CDI" = "Oxford CDI"))
  })

  output$form_selector <- renderUI({
    selectizeInput("form", label = h4("Form"),
                   choices = forms(), selected = input_form())
  })

  measures <- reactive({
    if ("WG" == input_form()) {
      list("Produces" = "produces", "Understands" = "understands")
    } else {
      list("Produces" = "produces")
    }
  })

  output$measure_selector <- renderUI({
    selectInput("measure", label = h4("Measure"),
                choices = measures(), selected = input_measure())
  })

  age_min <- reactive(instrument()$age_min)
  age_max <- reactive(instrument()$age_max)

  output$age_selector <- renderUI({
    sliderInput("age", label = h4("Age (Months)"),
                min = age_min(), max = age_max(), step = 1,
                value = c(age_min(), age_max()))
  })

  output$download_all <- downloadHandler(
    "item_data.csv",
    content <- function(file) {
      write.csv(data(), file, row.names = FALSE)
    })

  output$download_current <- downloadHandler(
    "item_data.csv",
    content <- function(file) {
      s <- as.numeric(input$table_rows_all)
      write.csv(data()[s, , drop = FALSE], file, row.names = FALSE)
    })

  output$download_selected <- downloadHandler(
    "item_data.csv",
    content <- function(file) {
      s <- as.numeric(input$table_rows_selected)
      write.csv(data()[s, , drop = FALSE], file, row.names = FALSE)
    })

  output$loaded <- reactive(1)

})
