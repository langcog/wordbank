library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
library(lazyeval)
source("../app_themes.R")
source("../data_loading.R")

## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "production",
#              qsize = ".2", age = 25, demo = 'identity')

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
  
  items <- get.item.data(common.tables)
  
  instruments <- as.data.frame(common.tables$instrument)  
  
  languages <- sort(unique(instruments$language))
  
  possible_demo_fields <- list("None" = "identity", 
                               "Birth Order" = "birth.order", 
                               "Ethnicity" = "ethnicity",
                               "Sex" = "sex",
                               "Mother's Education" = "momed.level")
  
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
  
  input.age <- reactive({
    ifelse(is.null(input$measure), floor((age.min()+age.max())/2), input$age)
  })
  
  input.demo <- reactive({
    ifelse(is.null(input$demo), start.demo(), input$demo)
  })
  
  instrument <- reactive({
    filter(instruments, language == input.language(), form == input.form())
  })
  
  num.words <- reactive({
    nrow(filter(items, language == input.language(), form == input.form(), type == "word"))
  })
  
  bin_size <- reactive({
    as.numeric(input$bin_size) / num.words()
  })
  
  cuts <- reactive({
    seq(0.0, 1.0, by=as.numeric(input$qsize))
  })
  
  middles <- reactive({
    cuts()[2:length(cuts())] - as.numeric(input$qsize)/2
  })
  
  filtered_admins <- reactive({
    admins %>%
      filter(language == input.language(),
             form == input.form(),
             measure == input.measure(),
             age == input.age())
  })
  
  groups_with_data <- reactive({
    filtered_admins() %>%
      group_by_(input.demo()) %>%
      summarise(n = n()) %>%
      filter_(interp("!is.na(x)", x = as.name(input.demo())))
  })
  
  data <- reactive({
    filtered_admins() %>%
      right_join(groups_with_data()) %>%
      group_by_("age", input.demo()) %>%
      filter_(interp("!is.na(x)", x = as.name(input.demo()))) %>%
      mutate(prop.vocab = vocab / num.words(),
             percentile = rank(prop.vocab) / length(prop.vocab),
             quantile = cut(percentile,
                            breaks=cuts(), 
                            labels=middles()))
  })
  
  plot <- function() {
    ggplot(data(), aes(x=prop.vocab, fill=quantile)) + 
      facet_wrap(input.demo()) + 
      geom_histogram(binwidth = bin_size()) +
      scale_x_continuous(name="\nVocabulary Size (proportion of total words)",
                         limits=c(0,1)) +
      ylab("Number of Children\n") + 
      scale_fill_brewer(name="Quantile\nMidpoint",
                        palette=seq.palette) +
      theme(text=element_text(family=font))
  }
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(instruments,
                                                   language == input.language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
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
    session$clientData$output_plot_width * 0.7
  })
  
  output$sample_size_header <- renderText({"Sample sizes:"})
  output$sample_size <- renderTable({
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
  
  age.min <- reactive({instrument()$age_min})
  age.max <- reactive({instrument()$age_max})
  
  output$age_selector <- renderUI({
    sliderInput("age", label = h4("Age (Months)"), 
                min = age.min(), max = age.max(), step = 1,
                value = input.age())
  })
  
  output$demo_selector <- renderUI({
    
    num_demo_values <- function(demo) {
      groups <- filtered_admins() %>%
        filter_(interp("!is.na(x)", x = as.name(demo))) %>%
        group_by_(demo) %>%
        summarise(n = n())
      return(length(groups[[demo]]))
    }
    
    demo_fields <- Filter(function(demo) demo == "identity" | num_demo_values(demo) >= 2,
                          possible_demo_fields)
    selectInput("demo", label = h4("Split Variable"),
                choices = demo_fields, selected = input.demo())
  })
    
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_distribution.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_distribution.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
  output$loaded <- reactive({1})
  
})
