library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(lazyeval)
library(quantregGrowth)
library(wordbankr)
library(langcog)
library(purrr)
source("predictQR_fixed.R")
theme_set(theme_mikabr(base_size = 18))
mode <- "local"

input <- list(language = "English", form = "WS", measure = "production",
              quantiles = "Standard", demo = "sex")

alerted <- FALSE

shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  admins <- get_administration_data(mode = mode, original_ids = TRUE) %>%
    gather(measure, vocab, comprehension, production) %>%
    mutate(identity = "All Data")

  instruments <- get_instruments(mode)
  languages <- sort(unique(instruments$language))

  possible_demo_fields <- list("None" = "identity",
                               "Birth Order" = "birth_order",
                               "Ethnicity" = "ethnicity",
                               "Gender" = "sex",
                               "Mother's Education" = "mom_ed")
  min_obs <- 100

  start_language <- "English"
  start_form <- "WS"
  start_measure <- "production"
  start_demo <- "identity"

  input_language <- reactive({
    input$language
    #ifelse(is.null(input$language), start_language, input$language)
  })

  input_form <- reactive({
    ifelse(is.null(input$form), start_form, input$form)
  })

  input_measure <- reactive({
    ifelse(is.null(input$measure), start_measure, input$measure)
  })

  input_demo <- reactive({
    ifelse(is.null(input$demo), start_demo, input$demo)
  })

  input_cross_sectional <- reactive({
    'cross_sectional' %in% input$data_filter
  })

  input_norming <- reactive({
    'norming' %in% input$data_filter
  })

  input_quantiles <- reactive({
    switch(input$quantiles,
           Standard = c(0.10, 0.25, 0.50, 0.75, 0.90),
           Deciles = c(0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90),
           Quintiles = c(0.20, 0.40, 0.60, 0.80),
           Quartiles = c(0.25, 0.50, 0.75),
           Median = c(0.5))
  })

  instrument <- reactive({
    instruments %>% filter(language == input_language(), form == input_form())
  })

  age_min <- reactive(instrument()$age_min)
  age_max <- reactive(instrument()$age_max)

  ylabel <- reactive({
    if (input_measure() == "comprehension") {
      "Size of Receptive Vocabulary"
    } else if (input_measure() == "production") {
      "Size of Productive Vocabulary"
    }
  })

  form_admins <- reactive({
    form_specific_admins <- admins %>%
      filter(language == input_language(),
             form == input_form(),
             measure == input_measure())

    #Compute cross-sectional as first entry for a child in a source
    first_longitudinals <- form_specific_admins %>%
      filter(longitudinal) %>%
      group_by(source_name, original_id) %>%
      arrange(age) %>%
      slice(1)

    form_specific_admins %>%
      mutate(cross_sectional = !longitudinal |
               (longitudinal & (data_id %in% first_longitudinals$data_id)))
  })

  filtered_admins <- reactive({

    filtered_admins <- form_admins()

    if(input_cross_sectional())
      filtered_admins <- filter(filtered_admins, cross_sectional == TRUE)

    if(input_norming())
      filtered_admins <- filter(filtered_admins, norming == TRUE)

    filtered_admins
  })

  clump_step <- function(groups, map, fun_demo) {
    if (fun_demo == "birth_order") {
      fine_groups <- groups[0:(nrow(groups) - 2),]
      small_groups <- slice(groups, (nrow(groups) - 1):nrow(groups))
      clump_demo <- small_groups$demo[1]
      clump <- data.frame(demo = clump_demo, n = sum(small_groups$n))
      clumped <- bind_rows(fine_groups, clump)
    } else if (fun_demo == "ethnicity") {
      fine_groups <- filter(groups, n >= min_obs & demo != "Other")
      small_groups <- filter(groups, n < min_obs | demo == "Other")
      clump_demo <- paste(small_groups$demo, collapse = ", ")
      clump <- data.frame(demo = clump_demo, n = sum(small_groups$n))
      clumped <- bind_rows(fine_groups, clump)
    } else if (fun_demo %in% c("sex", "mom_ed")) {
      smallest <- row.names(groups)[groups$n == min(groups$n)] %>% as.numeric()
      neighbor <- row.names(groups)[groups$n == min(groups[smallest - 1,]$n,
                                                    groups[smallest + 1,]$n,
                                                    na.rm = TRUE)] %>%
        as.numeric()
      small_groups <- slice(groups, c(smallest, neighbor))
      pre_fine_groups <- groups[0:(min(smallest, neighbor) - 1),]
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
      if (fun_demo == "birth_order" & nrow(groups) > 1) {
        demos <- unique(groups$demo)
        groups %<>% mutate(demo = c(as.character(demos[1:(length(demos) - 1)]),
                                    paste0(demos[length(demos)], "+")))
        plus <- max(which(names(map) == map))
        map[plus:length(map)] <- paste0(map[plus], "+")
      }
      groups %<>%
        filter(fun_demo == "identity" | n >= min_obs) %>%
        rename(clump = demo) %>%
        mutate(demo_label = sprintf("%s (n = %s)", clump, n))
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
    groups_map <- clumped_demo_groups(input_demo())
    groups <- groups_map$groups
    groups$clump <- factor(groups$clump, levels = groups$clump)
    groups$demo_label <- factor(groups$demo_label, levels = groups$demo_label)
    map <- groups_map$map
    demo_map <- data.frame(demo = names(map), clump = unlist(map),
                           row.names = NULL)
    demo_map$clump <- factor(demo_map$clump, levels = groups$clump)
    filtered_admins() %>%
      rename_(demo = input_demo()) %>%
      left_join(demo_map) %>%
      right_join(groups) %>%
      select(-demo) %>%
      rename(demo = clump)
  })

  fit_curves <- function() {

    models <- data() %>%
      group_by(demo) %>%
      do(model = gcrq(vocab ~ ps(age, monotone = 1, lambda = 1000),
                      data = ., tau = input_quantiles()))

    get_model <- function(demo.value) {
      return(filter(models, demo == value)$model[[1]])
    }

    predicted_data <- data.frame()
    values <- as.character(unique(data()$demo))

    for (value in values) {
      ages <- data.frame(age = age_min():age_max())
      value_predicted_data <- predictQR_fixed(get_model(value),
                                              newdata = ages) %>%
        as.data.frame() %>%
        mutate(age = age_min():age_max()) %>%
        gather(quantile, predicted, -age) %>%
        mutate(demo = value,
               quantile = factor(quantile))
      predicted_data <- bind_rows(predicted_data, value_predicted_data)
    }

    # TODO: when grcq fixes its bug, get rid of the if "." thing in curves
    if (predicted_data$quantile[1] == ".") {
      predicted_data$quantile <- factor(.5)
    }

    clump_groups <- clumped_demo_groups(input_demo())$groups %>%
      rename(demo = clump)

    quantile_label <- sprintf(
      "%.2f",
      as.numeric(levels(predicted_data$quantile))[predicted_data$quantile]
    )

    predicted_data %>%
      left_join(clump_groups) %>%
      mutate(demo = factor(demo, levels = clump_groups$demo),
             demo_label = factor(demo_label, levels = clump_groups$demo_label),
             quantile = sprintf(
               "%.2f", as.numeric(levels(predicted_data$quantile))[quantile]
             ))

  }

  curves <- reactive(tryCatch(fit_curves(), error = function(e) NULL))

  curves_bug <- observe({
    if (is.null(curves()) & !alerted) {
      createAlert(session, "curves_bug", "alert",
                  content = "The current model does not fit well to this dataset.",
                  style = "warning", dismiss = FALSE)
      alerted <<- TRUE
    }
    if (!is.null(curves()) & alerted) {
      closeAlert(session, "alert")
      alerted <<- FALSE
    }
  })

  plot <- reactive({
    req(data())

    pt_color <- "#839496"

    p <- ggplot(data(), aes(x = age, y = vocab)) +
      geom_jitter(size = .6, color = pt_color, alpha = .7) +
      scale_x_continuous(name = "\nAge (months)",
                         breaks = seq(age_min(), age_max(), by = 2),
                         limits = c(age_min(), age_max())) +
      scale_y_continuous(name = paste0(ylabel(), "\n"),
                         limits = c(0, max(data()$vocab)))

    if (input$quantiles == "Median") {
      if (!is.null(curves())) {
        colour_name <- names(which(possible_demo_fields == input_demo()))
        colour_values <- length(unique(curves()$demo)) %>% solarized_palette()
        p <- p +
          geom_line(aes(x = age, y = predicted, color = demo_label),
                    data = curves(), size = 1.5) +
          scale_color_manual(name = colour_name,
                             values = colour_values)
      }
    } else {
      p <- p +
        facet_wrap(~demo_label)
      if (!is.null(curves())) {
        colour_values <- length(unique(curves()$quantile)) %>%
          solarized_palette() %>%
          rev()
        p <- p +
          geom_line(aes(x = age, y = predicted, color = quantile),
                    data = curves(), size = 1.5) +
          scale_color_manual(name = "Quantile", values = colour_values) +
          guides(color = guide_legend(reverse = TRUE))
      }
    }
    p
  })

  forms <- reactive({
    form_opts <- unique(filter(instruments, language == input_language())$form)

    # can we do this functionally? this is simple though
    # still has hard-coded cases to deal with naming the opaque WS and WG designators
    forms <- list()
    for (opt in form_opts) {
      if (opt == "WS") {
        forms[["Words & Sentences"]] = "WS"
      } else if (opt == "WG") {
        forms[["Words & Gestures"]] = "WG"
      } else {
        forms[[opt]] <- opt
      }
    }

    return(forms)
  })

  # stopgap: hard code those forms that have a comprehension variable.
  # all others will be production-only for now.
  # in the end, this will need a specification in the instruments table.
  measures <- reactive({
    if (input_form() %in% c("WG", "FormA","IC")) {
      list("Produces" = "production", "Understands" = "comprehension")
    } else {
      list("Produces" = "production")
    }
  })

  height_fun <- function() session$clientData$output_plot_width * 0.7
  output$plot <- renderPlot(
    plot(), height = height_fun
    )

  table_data <- reactive({
    curves() %>%
      select(age, quantile, predicted, demo) %>%
      spread(quantile, predicted) %>%
      arrange(demo) %>%
      rename_(.dots = setNames("demo", input_demo()))
  })

  output$table <- renderTable(table_data(), include.rownames = FALSE,
                              digits = 1)

  output$language_selector <- renderUI({
    selectizeInput("language", label = strong("Language"),
                   choices = languages, selected = start_language)
  })

  output$form_selector <- renderUI({
    selectizeInput("form", label = strong("Form"),
                   choices = forms(), selected = input_form())
  })

  output$measure_selector <- renderUI({
    selectizeInput("measure", label = strong("Measure"),
                   choices = measures(), selected = input_measure())
  })

  output$data_filter <- renderUI({

    possible_filters =  c("cross-sectional only" = "cross_sectional",
                 "normative sample" = "norming")

    available_filters <- Filter(
      function(data_filter) !all(is.na(form_admins()[[data_filter]]) |
                              form_admins()[[data_filter]] == FALSE),
     possible_filters
    )



    checkboxGroupInput("data_filter", "Choose Data",
                       choices = available_filters,
                       selected = "cross_sectional")

  })

  output$demo_selector <- renderUI({
    available_demos <- Filter(
      function(demo) !all(is.na(filtered_admins()[[demo]])),
      possible_demo_fields
    )
    demo_fields <- Filter(
      function(demo) demo == "identity" |
        nrow(clumped_demo_groups(demo)$groups) >= 2,
      available_demos
    )
    selectInput("demo", label = strong("Split Variable"),
                choices = demo_fields, selected = input_demo())
  })

  output$download_table <- downloadHandler(
    filename = function() "vocabulary_norms_table.csv",
    content = function(file) {
      td <- table_data()
      extra_cols <- data.frame(language = rep(input_language(), nrow(td)),
                               form = rep(input_form(), nrow(td)),
                               measure = rep(input_measure(), nrow(td)))
      write.csv(bind_cols(extra_cols, td), file, row.names = FALSE)
    })

  output$download_data <- downloadHandler(
    filename = function() "vocabulary_norms_data.csv",
    content = function(file) {
      write.csv(data(), file, row.names = FALSE)
    })

  output$download_plot <- downloadHandler(
    filename = function() "vocabulary_norms.pdf",
    content = function(file) {
      cairo_pdf(file, width = 10, height = 7)
      print(plot())
      dev.off()
    })

  output$loaded <- reactive(1)

})
