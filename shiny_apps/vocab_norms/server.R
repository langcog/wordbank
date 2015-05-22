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
#load("~/Documents/projects/wordbank/shiny_apps/norms_app/debug.RData")

## DEBUGGING
# input <- list(language = "German", form = "WS", measure = "production",
#               quantiles = "Standard", demo = "sex")

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
                              labels=c("Asian", "Black", "Hispanic", "White", "Other/Mixed")),
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
  min_obs <- 100
  max_obs_diff <- 1000
  
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
  
  age.min <- reactive({instrument()$age_min})
  age.max <- reactive({instrument()$age_max})
  
  ylabel <- reactive({
    if (input.measure() == "comprehension") {
      "Size of Receptive Vocabulary"
    } else if (input.measure() == "production") {
      "Size of Productive Vocabulary"
    }
  })
    
  filtered_admins <- reactive({
    admins %>%
      filter(language == input.language(),
             form == input.form(),
             measure == input.measure()) 
  })
  
  clump_step <- function(groups, map, fun_demo) {
    if (fun_demo == "birth.order") {
      fine_groups <- groups[0:(nrow(groups)-2),]
      small_groups <- slice(groups, (nrow(groups)-1):nrow(groups))
      clump_demo <- small_groups$demo[1]
      clump <- data.frame(demo = clump_demo, n = sum(small_groups$n))
      clumped <- bind_rows(fine_groups, clump)
    } else if (fun_demo == "ethnicity") {
      fine_groups <- filter(groups, n >= min_obs & demo != "Other/Mixed")
      small_groups <- filter(groups, n < min_obs | demo == "Other/Mixed")
      clump_demo <- paste(small_groups$demo, collapse = ", ")
      clump <- data.frame(demo = clump_demo, n = sum(small_groups$n))
      clumped <- bind_rows(fine_groups, clump)
    } else if (fun_demo %in% c("sex", "momed.level")) {
      smallest <- as.numeric(row.names(groups)[groups$n == min(groups$n)])
      neighbor <- as.numeric(row.names(groups)[groups$n == min(groups[smallest - 1,]$n,
                                                               groups[smallest + 1,]$n,
                                                               na.rm = TRUE)])
      small_groups <- slice(groups, c(smallest, neighbor))
      pre_fine_groups <- groups[0:(min(smallest, neighbor)-1),]
      if (max(smallest, neighbor) == nrow(groups)) {
        post_fine_groups <- NULL
      } else {
        post_fine_groups <- groups[(max(smallest, neighbor) + 1):nrow(groups),]
      }
      clump_demo <- paste(small_groups$demo, collapse = ", ")
      clump <- data.frame(demo = clump_demo, n = sum(small_groups$n))
      clumped <- bind_rows(pre_fine_groups, clump, post_fine_groups)
    }
    for (small_demo in small_groups$demo) {
      map[[small_demo]] <- as.character(clump_demo)
      map[which(map == small_demo)] <- as.character(clump_demo)
    }
    return(list("clumped" = clumped, "map" = map))
  }
  
  clump_demo_groups <- function(groups, map, fun_demo) {
    if (all(groups$n >= min_obs) | nrow(groups) == 1) {
      if (fun_demo == "birth.order" & nrow(groups) > 1) {
        demos <- unique(groups$demo)
        groups %<>% mutate(demo = c(as.character(demos[1:(length(demos)-1)]),
                                    paste0(demos[length(demos)], "+")))
        plus <- max(which(names(map) == map))
        map[plus:length(map)] <- paste0(map[plus], "+")
      }
      groups %<>%
        filter(fun_demo == "identity" | n >= min_obs) %>%
        rename(clump = demo)
      return(list("groups" = groups, "map" = map))
    } else {
      step <- clump_step(groups, map, fun_demo)
      clumped_groups <- step$clumped
      clump_map <- step$map
      return(clump_demo_groups(clumped_groups, clump_map, fun_demo))
    }
  }

  clumped_demo_groups <- function(fun_demo) {
    demo_groups <- filtered_admins() %>%
      rename_(demo = fun_demo) %>%
      filter(!is.na(demo)) %>%
      group_by(demo) %>%
      summarise(n = n())
    map <- as.list(as.character(demo_groups$demo))
    names(map) <- map
    clump_demo_groups(demo_groups, map, fun_demo)
  }
  
  data <- reactive({
    groups_map <- clumped_demo_groups(input.demo())
    groups <- groups_map$groups
    groups$clump <- factor(groups$clump, levels = groups$clump)
    map <- groups_map$map
    demo_map <- data.frame(demo = names(map), clump = unlist(map), row.names = NULL)
    demo_map$clump <- factor(demo_map$clump, levels = groups$clump)
    filtered_admins() %>%
      rename_(demo = input.demo()) %>%
      left_join(demo_map) %>%
      right_join(groups) %>%
      select(-demo) %>%
      rename(demo = clump)
  })
    
  fit_curves <- function() {
    
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
    
    # TODO: when grcq fixes its bug, get rid of the if "." thing in curves
    if (predicted.data$quantile[1] == ".") {
      predicted.data$quantile <- factor(.5) 
    }
    
    groups_map <- clumped_demo_groups(input.demo())
    groups <- groups_map$groups
    groups$clump <- factor(groups$clump, levels = groups$clump)
    
    clump_levels <- clumped_demo_groups(input.demo())$groups$clump
    predicted.data %>%
      mutate(demo = factor(demo, levels = clump_levels),
             quantile = sprintf("%.2f", as.numeric(levels(predicted.data$quantile))[predicted.data$quantile]))
    
  }
  
  curves <- reactive({
    tryCatch({fit_curves()}, error = function(e) NULL)
  })
  
  plot <- function() {
    
    pt.color <- "#657b83"
    
    p <- ggplot(data(), aes(x = age, y = vocab)) +
      geom_jitter(width = 0.1, size = 1, color = pt.color) +
      scale_x_continuous(name = "\nAge (months)",
                         breaks = seq(age.min(), age.max(), by = 2),
                         limits = c(age.min(), age.max())) +
      scale_y_continuous(name = paste0(ylabel(), "\n"),
                         limits = c(0, max(data()$vocab))) +
      theme(text = element_text(family = font))
    
    if (input$quantiles == "Median") {
      if (!is.null(curves())) {
        p <- p +
          geom_line(data = curves(), size = 1, aes(x = age, y = predicted, color = demo)) +
          scale_color_manual(name = names(which(possible_demo_fields == input.demo())),
                             values = color_palette(length(unique(curves()$demo))))
      }        
    } else {
      p <- p +
        facet_wrap(~ demo)
      if (!is.null(curves())) {
        p <- p +
          geom_line(data = curves(), size = 1, aes(x = age, y = predicted, color = quantile)) +
          scale_color_manual(name = "Quantile",
                           values = rev(color_palette(length(unique(curves()$quantile))))) +
          guides(color = guide_legend(reverse = TRUE))
      }
    }
    p
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
    clumped_demo_groups(input.demo())$groups
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
    available_demos <- Filter(function(demo) !all(is.na(filtered_admins()[[demo]])),
                              possible_demo_fields)
    demo_fields <- Filter(function(demo) demo == "identity" | nrow(clumped_demo_groups(demo)$groups) >= 2,
                          available_demos)
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
      cairo_pdf(file, width = 10, height = 10*aspect.ratio(), family = font)
      print(plot())
      dev.off()
    })
  
  output$loaded <- reactive({1})
  
})
