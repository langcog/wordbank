library(shiny)
library(dplyr)
library(magrittr)
library(wordbankr)
mode <- "local"

#input <- list(language = "English", form = "WS", age = c(18, 30))

shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  admins <- get_administration_data(mode = mode) %>%
    select(data_id, language, form, age, sex, mom_ed, comprehension, production) %>%
    rename(gender = sex)


  input_language <- reactive({
    ifelse(is.null(input$language), "All", input$language)
  })

  input_form <- reactive({
    ifelse(is.null(input$form), "All", input$form)
  })

  input_gender <- reactive({
    ifelse(is.null(input$gender), "All", input$gender)
  })

  input_mom_ed <- reactive({
    ifelse(is.null(input$mom_ed), "All", input$mom_ed)
  })

  input_age <- reactive({
    if (is.null(input$age)) c(min(admins$age), max(admins$age))  else input$age
  })

  data <- reactive({
    filter.data <- admins
    if (input_language() != "All") {
      filter.data %<>% filter(language == input_language())
    }
    if (input_form() != "All") {
      filter.data %<>% filter(form == input_form())
    }
    if (input_gender() != "All") {
      filter.data %<>% filter(gender == input_gender())
    }
    if (input_mom_ed() != "All") {
      filter.data %<>% filter(mom_ed == input_mom_ed())
    }
    filter.data %<>% filter(age >= input_age()[[1]], age <= input_age()[[2]])
    filter.data
  })

  output$table <- renderDataTable(data(), options = list(orderClasses = TRUE))

  output$language_selector <- renderUI({
    selectizeInput("language", label = "Language:",
                   choices = c("All", sort(unique(admins$language))),
                   selected = "All")
  })

  output$form_selector <- renderUI({
    selectizeInput("form", label = "Form:",
                   choices = c("All", list("Words & Sentences" = "WS",
                                           "Words & Gestures" = "WG",
                                           "Oxford CDI" = "Oxford CDI")),
                   selected = "All")
  })

  output$age_selector <- renderUI({
    sliderInput("age", label = "Age (Months):",
                min = min(admins$age), max = max(admins$age), step = 1,
                value = c(min(admins$age), max(admins$age)))
  })

  output$gender_selector <- renderUI({
    selectizeInput("gender", label = "Gender:",
                   choices = c("All", levels(unique(admins$gender))),
                   selected = "All")
  })

  output$momed_selector <- renderUI({
    selectizeInput("mom_ed", label = "Maternal Education:",
                   choices = c("All", levels(unique(admins$mom_ed))),
                   selected = "All")
  })

  output$download_data <- downloadHandler(
    filename = function() "administration_data.csv",
    content = function(file) write.csv(data(), file, row.names = FALSE)
  )

  output$loaded <- reactive(1)

})
