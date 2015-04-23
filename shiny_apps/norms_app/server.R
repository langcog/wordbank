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
# input <- list(language = "English", form = "WS", measure = "production",
#              qsize = ".2", demo = "birth.order")

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
#   wordbank <- src_mysql(dbname = "wordbank", user = "wordbank",
#                         password = "wordbank")
  wordbank <- src_mysql(dbname='wordbank', host="54.149.39.46", #54.200.225.86
                        user="wordbank", password="wordbank")
  
  
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
  
  instrument.tables <- get.instrument.tables(wordbank, common.tables$instrumentsmap)
  
  languages <- unique(instrument.tables$language)
  
  possible_demo_fields <- list("None" = "identity", 
                               "Birth Order" = "birth.order", 
                               "Ethnicity" = "ethnicity",
                               "Sex" = "sex",
                               "Mother's Education" = "momed.level")
  min_obs <- 100
  
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
  
  instrument <- reactive({filter(instrument.tables,
                                 language == input.language(),
                                 form == input.form())})
  
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
    seq(0.0, 1.0, by=as.numeric(input$qsize))
  })
  
  middles <- reactive({
    cuts()[2:length(cuts())] - as.numeric(input$qsize)/2
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
    renamed_filtered_admins() %>%
      group_by(demo) %>%
      summarise(n = n()) %>%
      filter(n > min_obs)
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
      do(model = gcrq(vocab ~ ps(age, monotone=1, lambda=60), data=., tau=middles()))
    
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
  
  plot <- function() {
    
    if (input$qsize == 1 & input.demo() == "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab)) +
        geom_jitter(width=.1, col = "steelblue") +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted),
                  size = 1, 
                  col = "steelblue") 
    } else if (input$qsize != 1 & input.demo() == "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab, col = quantile)) +
        geom_jitter(width=.1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, col = quantile),
                  size = 1) 
    } else if (input$qsize == 1 & input.demo() != "identity") {
      p <- ggplot(data(), aes(x=age, y=vocab, col = demo)) +
        geom_jitter(width=.1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, col = demo),
                  size = 1) 
    } else {
      p <- ggplot(data(), aes(x=age, y=vocab, col = demo)) +
        geom_jitter(width=.1) +    
        geom_line(data = curves(),
                  aes(x = age, y = predicted, col = demo),
                  size = 1) +
        facet_wrap(~quantile)
    }
    
    p + scale_x_continuous(name="\nAge (months)",
                         breaks=seq(age.min(), age.max(), by=2),
                         limits=c(age.min(), age.max())) +
      ylab(paste(ylabel(), "\n", sep="")) +
      scale_colour_brewer(name = input.demo(),
                          palette=seq.palette) +
      theme(text=element_text(family=font))
  }
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(instrument.tables,
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
  
  demos <- reactive({
    demo_fields <- possible_demo_fields
    for (i in seq(length(possible_demo_fields),1,-1)) {
      if (all(is.na(filtered_admins()[possible_demo_fields[[i]]]))) {
        demo_fields <- demo_fields[-i]
      }
    }
    return(demo_fields)
  })                            
  
  output$plot <- renderPlot({
    plot()
  }, height = function() {
    session$clientData$output_plot_width * aspect.ratio()
  })
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h4("Language"), 
                   choices = languages, selected = start.language())
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h4("Form"), 
                   choices = forms(), selected = start.form())
  })
  
  output$measure_selector <- renderUI({
    selectizeInput("measure", label = h4("Measure"), 
                   choices = measures(), selected = start.measure())
  })
  
  output$demo_selector <- renderUI({
    selectizeInput("demo", label = h4("Split Variable"), 
                   choices = demos(), selected = start.demo())
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
