library(shiny)
library(readr)
library(dplyr)
library(ggplot2)
library(langcog)
library(feather)
theme_set(theme_mikabr(base_size = 14))
# font <- theme_mikabr()$text$family

all_prop_data <- feather::read_feather("all_prop_data.feather")
uni_lemmas <- sort(unique(all_prop_data$uni_lemma))
start_lemma <- "dog"
start_measure <- "produces"
kid_min <- 3
points_min <- 3


input <- list(uni_lemma = "crocodile",
              measure = "understands")


shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  output$uni_lemma <- renderUI({
    selectInput("uni_lemma", label = h4("Meaning"),
                choices = setNames(uni_lemmas, toupper(uni_lemmas)),
                selected = start_lemma)
  })

  output$measure_selector <- renderUI({
    selectInput("measure", label = h4("Measure"),
                choices = c("Produces" = "produces", "Understands" = "understands"),
                selected = start_measure)
  })

  uni_lemma_data <- function() {
    req(input$uni_lemma)
    all_prop_data %>%
      group_by(language) %>%
      filter(uni_lemma == input$uni_lemma &
               measure == input$measure &
               n >= kid_min &
               n() >= points_min)
  }

  n_languages <- function() {
    length(unique(uni_lemma_data()$language))
  }

  crosslinguistic_plot <- function() {
    words_data <- uni_lemma_data() %>%
      select(language, measure, words) %>%
      distinct()
    ggplot(uni_lemma_data(), aes(x = age)) +
      facet_wrap( ~ language, ncol = min(n_languages(), 5)) +
      geom_point(aes(y = prop, colour = language)) +
      geom_smooth(aes(y = prop, colour = language), method = "loess", se = FALSE,
                  size = 1.5, span = 1) +
      # geom_line(aes(y = fit_prop, colour = language), size = 1.5) +
      geom_label(aes(x = 8, y = 1, label = words), data = words_data,
                 label.padding = unit(0.15, "lines"),
                 vjust = "inward", hjust = "inward") +
      scale_colour_solarized(guide = FALSE) +
      scale_fill_solarized(guide = FALSE) +
      scale_y_continuous(name = "Proportion of children\n", limits = c(0, 1)) +
      scale_x_continuous(name = "\nAge (months)", limits = c(8, 18),
                         breaks = seq(8, 18, 2))
  }

  output$crosslinguistic <- renderPlot({
    crosslinguistic_plot()
  }, height = function() ceiling(n_languages()/5) * 125 + 100, width = function() min(n_languages(), 5)* 125 + 100)

  table_data <- reactive({
    uni_lemma_data() %>%
      select(language, age, measure, uni_lemma, words, prop)
  })

  output$table <- renderTable({
    table_data()
  }, include.rownames = FALSE, digits = 2)

  output$download_table <- downloadHandler(
    filename = function() "crosslinguistic_table.csv",
    content = function(file) {
      write_csv(table_data(), file)
    })

  output$download_plot <- downloadHandler(
    filename = function() "crosslinguistic.pdf",
    content = function(file) {
      cairo_pdf(file, width = 10, height = 6)
      print(crosslinguistic_plot())
      dev.off()
    })

  output$loaded <- reactive(1)

})
