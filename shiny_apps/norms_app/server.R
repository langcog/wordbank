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
source("../data_loading.R")
source("predictQR_fixed.R")
# options(shiny.error=browser)

## DEBUGGING
input <- list(language = "Hebrew", form = "WG", measure = "production",
             num_quantiles = 3, demo = "identity")

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  

  wordbank <- connect.to.wordbank("local")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables$momed,
                                    common.tables$child,
                                    common.tables$instrumentsmap,
                                    common.tables$administration) %>%
    gather(measure, vocab, comprehension, production) %>%
    mutate(identity = "All Data") %>%
    mutate(sex = factor(sex, levels=c("F", "M", "O"), labels=c("Female", "Male", "Other")),
           ethnicity = factor(ethnicity, levels=c("A", "B", "H", "O", "W"),
                              labels=c("Asian", "Black", "Hispanic", "Other/Mixed", "White")),
           birth.order = factor(birth.order, level = c(1, 2, 3, 4, 5, 6, 7, 8),
                                labels = c("First", "Second", "Third", "Fourth", "Fifth",
                                           "Sixth", "Seventh", "Eighth")))
  
  instruments <- as.data.frame(common.tables$instrumentsmap)  

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
  
  aspect.ratio <- reactive({
    base <- 0.7
    scaling <- 1
    #     panels <- nrow(select_(groups_with_data(), input.demo()))
    #     if (panels == 2) {
    #       scaling <- 1/2
    #     } else if (panels == 3) {
    #       scaling <- 1/3
    #     } else if (panels == 4) {
    #       scaling <- 1/1
    #     } else if (panels == 6) {
    #       scaling <- 2/3
    #     }
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
  
  cuts <- reactive({
    seq(0.0, 1.0, by=1/as.numeric(input$num_quantiles))
  })
  
  middles <- reactive({
    round(cuts()[2:length(cuts())] - 1/as.numeric(input$num_quantiles)/2, 2)
  })
  
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

  groups_with_data <- reactive({
    groups <- renamed_filtered_admins() %>%
      group_by(demo) %>%
      summarise(n = n()) %>%
      filter(n >= min_obs)
  })
  
  data <- reactive({
    renamed_filtered_admins() %>%
      right_join(groups_with_data()) %>%
      group_by(age, demo) %>%
      mutate(percentile = rank(vocab) / length(vocab),
             quantile = cut(percentile,
                            breaks=cuts(),
                            labels=middles()))
  })

# TODO: when grcq fixes its bug, get rid of the if "." thing in curves

  curves <- reactive({
    
    clean.data <- renamed_filtered_admins() %>%
      right_join(groups_with_data())
    
    models <- clean.data %>%
      group_by(demo) %>%
      do(model = gcrq(vocab ~ ps(age, monotone=1, lambda=1000), 
                      data=., tau=middles()))
    
    get.model <- function(demo.value) {
      return(filter(models, demo==value)$model[[1]])
    }
    
    predicted.data <- data.frame()
    values <- as.character(unique(clean.data$demo))
    
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
      mutate(demo = as.factor(demo))
  })
  
  color.legend.name <- reactive({
    if (input.demo() == "identity") {
      "Quantile"
    } else {
      names(which(possible_demo_fields == input.demo()))
    }
  })

  plot <- function() {
    
    pt.color <- "steelblue"
    
    # no faceting, no coloring
    if (input$num_quantiles == 1 & input.demo() == "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab)) +
        geom_jitter(width=.1, color = pt.color, size = 1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted),
                  size = 1, 
                  col = pt.color)
      
    # no faceting, color by quantile
    } else if (input$num_quantiles != 1 & input.demo() == "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab, color = quantile)) +
        geom_jitter(width=.1, color = pt.color, size = 1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, color = quantile),
                  size = 1) 
      
    # no faceting, color by demo
    } else if (input$num_quantiles == 1 & input.demo() != "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab, color = demo)) +
        geom_jitter(width=.1, size = 1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, color = demo),
                  size = 1) 
    
    # facet by quantile, color by demo
    } else {
      p <- ggplot(data(), aes(x=age, y=vocab, col = demo)) +
        geom_jitter(width=.1, size = 1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, col = demo),
                  size = 1) +
        facet_wrap(~quantile)
    }
    
    p + scale_x_continuous(name="\nAge (months)",
                         breaks=seq(age.min(), age.max(), by=2),
                         limits=c(age.min(), age.max())) +
      ylab(paste(ylabel(), "\n", sep="")) +
      scale_colour_brewer(name = color.legend.name(),
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
    session$clientData$output_plot_width * aspect.ratio()
  })
  
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
#demo_fields <- possible_demo_fields
#     for (i in seq(length(possible_demo_fields),1,-1)) {
#       if (all(is.na(filtered_admins()[possible_demo_fields[[i]]]))) {
#         demo_fields <- demo_fields[-i]
#       }
#    }
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
