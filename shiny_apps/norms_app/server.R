library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
library(lazyeval)
library(quantregGrowth)
source("../app_themes.R")
source("../palette.R")
source("../data_loading.R")
source("predictQR_fixed.R")

## DEBUGGING
input <- list(language = "English", form = "WS", measure = "production",
              quantiles = "Standard", demo = "identity")

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
  wordbank <- connect.to.wordbank("local")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables) %>%
    gather(measure, vocab, comprehension, production) %>%
    mutate(identity = "All Data") %>%
    mutate(sex = factor(sex, levels=c("F", "M", "O"), labels=c("Female", "Male", "Other")),
           ethnicity = factor(ethnicity, levels=c("A", "B", "H", "O", "W"),
                              labels=c("Asian", "Black", "Hispanic", "Other/Mixed", "White")),
           birth.order = factor(birth.order, level = c(1, 2, 3, 4, 5, 6, 7, 8),
                                labels = c("First", "Second", "Third", "Fourth", "Fifth",
                                           "Sixth", "Seventh", "Eighth")))
  
  instruments <- as.data.frame(common.tables$instrument)  
  
  languages <- sort(unique(instruments$language))
  
  possible_demo_fields <- list("None" = "identity", 
                               "Birth Order" = "birth.order", 
                               "Ethnicity" = "ethnicity",
                               "Sex" = "sex",
                               "Mother's Education" = "momed.level")
  min_obs <- 60
  
  start.language <- function() {"English"}
  start.form <- function() {"WS"}
  start.measure <- function() {"production"}
  start.demo <- function() {"identity"}
  
  
  input.language <- reactive({
    ifelse(is.null(input$language), start.language(), input$language)
  })
  
  input.form <- reactive({
    ifelse(is.null(input$form), start.form(), input$form)
  })
  
  input.measure <- reactive({
    ifelse(is.null(input$measure), start.measure(), input$measure)
  })
  
  input.demo <- reactive({
    ifelse(is.null(input$demo), start.demo(), input$demo)
  })
  
  input.quantiles <- reactive({
    switch(input$quantiles,
           Standard = c(0.10, 0.25, 0.50, 0.75, 0.90),
           Deciles = c(0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90),
           Quintiles = c(0.20, 0.40, 0.60, 0.80),
           Quartiles = c(0.25, 0.50, 0.75),
           Median = c(0.5))
  })
  
  aspect.ratio <- reactive({
    base <- 0.7
    scaling <- 1
    base * scaling
  })
  
  instrument <- reactive({
    filter(instruments, language == input.language(), form == input.form())
  })
  
  ylabel <- reactive({
    if (input.measure() == "comprehension") {
      "Size of Receptive Vocabulary"
    } else if (input.measure() == "production") {
      "Size of Productive Vocabulary"
    }
  })
  
  age.min <- reactive({instrument()$age_min})
  age.max <- reactive({instrument()$age_max})
    
  filtered_admins <- reactive({
    admins %>%
      filter(language == input.language(),
             form == input.form(),
             measure == input.measure()) 
  })
  
  renamed_filtered_admins <- reactive({
    filtered_admins() %>%
      rename_(demo = input.demo()) %>%    
      filter(!is.na(demo))
  })
  
  demo_groups <- reactive({
    renamed_filtered_admins() %>%
      group_by(demo) %>%
      summarise(n = n()) %>%
      filter(n >= min_obs)
  })
  
  data <- reactive({
    renamed_filtered_admins() %>%
      right_join(demo_groups())
  })
  
  # TODO: when grcq fixes its bug, get rid of the if "." thing in curves
  
  curves <- reactive({
    
    models <- data() %>%
      group_by(demo) %>%
      do(model = gcrq(vocab ~ ps(age, monotone = 1, lambda = 1000), 
                      data = ., tau = input.quantiles()))
    
    get.model <- function(demo.value) {
      return(filter(models, demo == value)$model[[1]])
    }
    
    predicted.data <- data.frame()
    values <- as.character(unique(data()$demo))
    
    for (value in values) {
      ages <- data.frame(age = age.min():age.max())
      value.predicted.data <- predictQR_fixed(get.model(value), newdata = ages) %>%
        as.data.frame() %>%
        mutate(age = age.min():age.max()) %>%
        gather(quantile, predicted, -age) %>%
        mutate(demo = value)
      predicted.data <- bind_rows(predicted.data, value.predicted.data)
    }
    
    if (predicted.data$quantile[1] == ".") {
      predicted.data$quantile <- factor(.5) 
    }
    
    predicted.data %>%
      mutate(demo = as.factor(demo),
             quantile = sprintf("%.2f", as.numeric(levels(predicted.data$quantile))[predicted.data$quantile]))
    
  })
  
  plot <- function() {
    
    pt.color <- "#657b83"
    
    p <- ggplot(data(), aes(x = age, y = vocab)) +
      geom_jitter(width = 0.1, size = 1, color = pt.color) +
      scale_x_continuous(name = "\nAge (months)",
                         breaks = seq(age.min(), age.max(), by = 2),
                         limits=c(age.min(), age.max())) +
      ylab(paste(ylabel(), "\n", sep = "")) +
      theme(text=element_text(family=font))
    
    if (input$quantiles == "Median") {
      p +
        geom_line(data = curves(), size = 1,aes(x = age, y = predicted, color = demo)) +
        scale_color_manual(name = names(which(possible_demo_fields == input.demo())),
                           values = rev(color_palette(length(unique(curves()$demo)))))
    } else {
      p +
        geom_line(data = curves(), size = 1, aes(x = age, y = predicted, color = quantile)) +
        scale_color_manual(name = "Quantile",
                           values = rev(color_palette(length(unique(curves()$quantile))))) +
        guides(color = guide_legend(reverse = TRUE)) +
        facet_wrap(~ demo)
    }
  }
  
  forms <- reactive({
    Filter(function(form) {
      form %in% unique(filter(instruments, language == input.language())$form)
    }, list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
  })
  
  measures <- reactive({
    if (input.form() == "WG") {
      list("Produces" = "production", "Understands" = "comprehension")
    } else if (input.form() == "WS") {
      list("Produces" = "production")
    }
  })
  
  output$plot <- renderPlot({
    plot()
  }, height = function() {
    session$clientData$output_plot_width * aspect.ratio()
  })
  
  output$sample_sizes <- renderTable({
    groups_with_data()
  }, include.rownames = FALSE, include.colnames = FALSE)
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"), 
                   choices = languages, selected = input.language())
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"), 
                   choices = forms(), selected = input.form())
  })
  
  output$measure_selector <- renderUI({
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures(), selected = input.measure())
  })
  
  output$demo_selector <- renderUI({
    
    num_demo_values <- function(demo) {
      groups <- filtered_admins() %>%
        filter_(interp("!is.na(x)", x = as.name(demo))) %>%
        group_by_(demo) %>%
        summarise(n = n()) %>%
        filter(n >= min_obs)
      return(length(groups[[demo]]))
    }
    
    demo_fields <- Filter(function(demo) demo == "identity" | num_demo_values(demo) >= 2,
                          possible_demo_fields)
    selectInput("demo", label = h4("Split Variable"),
                choices = demo_fields, selected = input.demo())
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_norms.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_norms.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=10*aspect.ratio(), family=font)
      print(plot())
      dev.off()
    })
  
  output$loaded <- reactive({1})
  
})
