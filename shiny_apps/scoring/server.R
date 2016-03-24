library(shiny)
library(dplyr)
library(readr)
library(tidyr)

shinyServer(function(input, output) {
  ## uploaded datafile
  infile <- reactive({
    input$file1
  })

  ## parse uploaded data
  data <- reactive({
    if (is.null(infile())) {
      d <- read_csv("sample.csv")
    } else {
      d <- read_delim(file = infile()$datapath,
                      quote = input$quote,
                      delim = input$sep)
    }
  })

  ## select vocab to use
  vocab_data <- reactive({
    read_csv("ws_english_lookup.csv")
  })

  ## merge data with vocab
  # deal with floor effects
  merged_data <- reactive({
    if (is.null(infile())) {
      data() %>%
        mutate(instrument = input$instrument) %>%
        left_join(vocab_data())
    } else {
      validate(
        need(input$age_col != "", "Please select an age column!"),
        need(input$vocab_col != "", "Please select a vocabulary column!"),
        need(input$gender_col != "", "Please select a gender column!")
      )

      data() %>%
        mutate(instrument = input$instrument) %>%
        rename_("age_months" = input$age_col,
                "vocab_nwords" = input$vocab_col,
                "gender" = input$gender_col) %>%
        mutate(age_months = floor(age_months),
               gender = ifelse(gender == input$male_val, "male", "female")) %>%
        left_join(vocab_data())
    }
  })

  ## UI selector for age column
  output$ageColumn <- renderUI({
    if (!is.null(infile())) {
      selectizeInput("age_col", "Column label in your data for ages (months)",
                     choices = c("",names(data())),
                     selected = "")
    }
  })

  ## UI selector for age column
  output$nwordsColumn <- renderUI({
    if (!is.null(infile())) {
      selectizeInput("vocab_col", "Column label in your data for vocabulary (number of words)",
                     choices = c("", names(data())),
                     selected = "")
    }
  })

  ## UI selector for gender column
  output$genderColumn <- renderUI({
    if (!is.null(infile())) {
      selectizeInput("gender_col", "Column label in your data for gender",
                     choices = c("", names(data())),
                     selected = "")
    }
  })

  ## UI selector for gender mappings
  output$genderMappings <- renderUI({
    if (!is.null(infile())) {
      selectizeInput("male_val", "Value in your gender column for males",
                     choices = c(unique(data()[,input$gender_col])))
    }
  })

  ## table title
  output$tableTitle <- renderUI({
    if (is.null(infile())) {
      list(
        h3("Sample merged output"),
        p("This is a sample of what your data would look like after scoring.")
      )
    } else {
        h3("Your scored output")
    }
  })

  ## render downlad button in case of a merge
  output$download <- renderUI({
    if (!is.null(infile())) {
      downloadButton('downloadData', 'Download')
    }
  })

  ## download merged data
  output$downloadData <- downloadHandler(
    filename = function() {
      paste0("percentiles.csv")
    },
    content = function(file) {
      write_csv(merged_data(), file)
    }
  )

  ## download sample data
  output$downloadSample <- downloadHandler(
    filename = function() {
      paste0("sample.csv")
    },
    content = function(file) {
      file.copy('sample.csv', file)
    }
  )

  ## render table of output
  output$contents <- DT::renderDataTable(merged_data(), style = "bootstrap",
                                         rownames = FALSE)
})
