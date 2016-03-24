library(shiny)
library(dplyr)
library(DT)
library(wordbankr)
mode <- "local"

#input <- list(language = "English", form = "WS", age = c(18, 30))

shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  instruments <- get_instruments(mode = mode)
  languages <- sort(unique(instruments$language))

  start_language <- "English"
  start_form <- "WS"

  data <- eventReactive(input$get_data, {

    req(input$language, input$form)

    get_instrument_data(input$language, input$form,
                        administrations = TRUE,
                        iteminfo = TRUE,
                        mode = mode) %>%
      select(data_id, age, sex, mom_ed, value, item_id, type, category,
             definition) %>%
      arrange(data_id)

  })

  output$table <- DT::renderDataTable(
    data(), filter = "top", style = "bootstrap", rownames = FALSE,
    options = list(orderClasses = TRUE, processing = TRUE, pageLength = 25)
  )

  output$language_selector <- renderUI({
    selectizeInput("language", label = h4("Language"),
                   choices = languages, selected = start_language)
  })

  forms <- reactive({
    req(input$language)
    valid_form <- function(form) {
      form %in% unique(filter(instruments,
                              language == input$language)$form)
    }
    Filter(valid_form, list("Words & Sentences" = "WS",
                            "Words & Gestures" = "WG"))
  })

  output$form_selector <- renderUI({
    selectizeInput("form", label = h4("Form"),
                   choices = forms(), selected = start_form)
  })

  output$download_button <- renderUI({
    if (!is.null(data())) {
      downloadButton("download_data", "Download Data",
                     class = "btn-xs")
    }
  })

  output$download_data <- downloadHandler(
    filename = function() "instrument_data.csv",
    content = function(file) {
      cat(nrow(data()))
      write.csv(data(), file, row.names = FALSE)
    })

  output$loading <- renderImage(list(src = "../images/loading.gif",
                                     contentType = "image/gif",
                                     alt = "Loading"),
                                deleteFile = FALSE)

  output$loaded <- reactive(1)

})
