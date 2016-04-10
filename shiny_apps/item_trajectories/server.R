library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(purrr)
library(ggplot2)
library(directlabels)
library(wordbankr)
library(langcog)
theme_set(theme_mikabr(base_size = 18))
font <- theme_mikabr()$text$family
Sys.setlocale(locale = "en_US.UTF-8")
mode <- "local"

# input <- list(language = "English", form = "WG WS", measure = "produces",
#               words = c("baa baa", "woof"))

list_items_by_definition <- function(item_data) {
  items <- item_data$item_id
  names(items) <- item_data$definition
  return(items)
}

list_items_by_id <- function(item_data) {
  items <- item_data$definition
  names(items) <- item_data$item_id
  return(items)
}

trajectory_data_fun <- function(admins, fun_instrument, fun_measure,
                                fun_words) {

  instrument_word_data <- function(inst_id) {
    inst <- filter(fun_instrument, instrument_id == inst_id)
    word_ids <- inst$words_by_definition[[1]][fun_words]
    get_instrument_data(instrument_language = inst$language,
                        instrument_form = inst$form,
                        items = word_ids[!is.na(word_ids)],
                        administrations = admins,
                        mode = mode) %>%
      mutate(instrument_id = inst_id)
  }

  if (!is.null(fun_words)) {
    word_data <- map(fun_instrument$instrument_id, instrument_word_data) %>%
      bind_rows() %>%
      mutate(produces = value == "produces",
             understands = value == "understands" | value == "produces") %>%
      select(-value) %>%
      gather(measure, value, produces, understands) %>%
      filter(measure == fun_measure) %>%
      filter(!is.na(age)) %>%
      group_by(instrument_id, num_item_id, age) %>%
      summarise(total = n(),
                prop = sum(value, na.rm = TRUE) / total) %>%
                #num_true = sum(value, na.rm = TRUE),
                #num_false = n() - num_true) %>%
      group_by(instrument_id) %>%
      mutate(item_id = sprintf("item_%s", num_item_id)) %>%
      rowwise() %>%
      mutate(item = fun_instrument[fun_instrument$instrument_id == instrument_id,]$words_by_id[[1]][item_id],
      type = "word") %>%
      left_join(select(fun_instrument, instrument_id, form)) %>%
      select(-instrument_id, -item_id)
  } else {
    word_data <- data.frame()
  }

  word_data
}

admins <- get_administration_data(mode = mode, original_ids = TRUE)

items <- get_item_data(mode = mode) %>%
  mutate(definition = iconv(definition, from = "utf8", to = "utf8"))

instruments <- get_instruments(mode = mode)
languages <- sort(unique(instruments$language))

instrument_tables <- instruments %>%
  group_by(instrument_id) %>%
  do(words_by_definition = list_items_by_definition(
    filter(items, language == .$language, form == .$form, type == "word")
  ),
  words_by_id = list_items_by_id(
    filter(items, language == .$language, form == .$form, type == "word")
  )) %>%
  left_join(instruments)

start_language <- "English"
start_form <- "WS"
start_measure <- "produces"

alerted <- FALSE

shinyServer(function(input, output, session) {

  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)

  input_language <- reactive({
    if (is.null(input$language)) start_language else input$language
  })

  input_form <- reactive({
    if (is.null(input$form)) start_form else input$form
  })

  input_forms <- reactive(strsplit(input_form(), " ")[[1]])

  input_measure <- reactive({
    if (is.null(input$measure)) start_measure else input$measure
  })

  input_cross_sectional <- reactive({
    'cross_sectional' %in% input$data_filter
  })

  input_norming <- reactive({
    'norming' %in% input$data_filter
  })

  input_words <- reactive({
    if (is.null(input$words)) word_options()[1] else input$words
  })

  many_words <- observe({
    word_limit <- 9
    if (length(input_words()) >= word_limit & !alerted) {
      createAlert(session, "many_words", "alert",
                  content = HTML(sprintf("For a large number of words, consider using the %s app instead.",
                              a(href = "http://wordbank.stanford.edu/analyses?name=item_data",
                                "Item Data"))),
                  style = "warning", dismiss = FALSE)
      alerted <<- TRUE
    }
    if (length(input_words()) < word_limit & alerted) {
      closeAlert(session, "alert")
      alerted <<- FALSE
    }
  })

  instrument <- reactive({
    filter(instrument_tables, language == input_language(),
           form %in% input_forms())
  })

  form_admins <- reactive({
    form_specific_admins <- admins %>%
      filter(language == input_language())

    if(length(input_forms()) == 1)
      form_specific_admins %<>% filter(form == input_forms())

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

    if (input_cross_sectional())
      filtered_admins <- filter(filtered_admins, cross_sectional == TRUE)

    if (input_norming())
      filtered_admins <- filter(filtered_admins, norming == TRUE)

    filtered_admins
  })

  trajectory_data <- reactive({
    if (all(input_words() %in% word_options())) {
      trajectory_data_fun(filtered_admins(), instrument(), input_measure(), input_words()) %>%
        mutate(item = factor(item, levels = input_words()))
    } else {
      data.frame()
    }
  })

  mean_data <- reactive({
    trajectory_data() %>%
      group_by(form, type, age) %>%
      summarise(prop = mean(prop),
                total = sum(total)) %>%
      mutate(item = "mean")
  })

  ylabel <- reactive({
    if (input_measure() == "understands") "Proportion of Children Understanding"
    else if (input_measure() == "produces") "Proportion of Children Producing"
  })

  age_min <- reactive(min(instrument()$age_min))
  age_max <- reactive(max(instrument()$age_max))

  trajectory_plot <- function() {
    traj <- trajectory_data()
    if (nrow(traj) == 0) {
      ggplot(traj) +
        geom_point() +
        scale_x_continuous(name = "\nAge (months)",
                           breaks = age_min():age_max(),
                           limits = c(age_min(), age_max() + 3)) +
        scale_y_continuous(name = sprintf("%s\n", ylabel()),
                           limits = c(-0.01, 1),
                           breaks = seq(0, 1, 0.25))
    } else {
      amin <- age_min()
      amax <- age_max()
      g <- ggplot(traj, aes(x = age, y = prop, colour = item, fill = item, label = item)) +
        # geom_smooth(aes(linetype = type, weight = total), method = "glm",
        #             method.args = list(family = "binomial")) +
        geom_smooth(aes(linetype = type, weight = total), method = "loess",
                    se = TRUE) +
        geom_point(aes(shape = form)) +
        scale_shape_manual(name = "", values = c(20, 1), guide = FALSE) +
        scale_linetype_discrete(guide = FALSE) +
        scale_x_continuous(name = "\nAge (months)",
                           breaks = amin:amax,
                           limits = c(amin, amax + 3)) +
        scale_y_continuous(name = sprintf("%s\n", ylabel()),
                           limits = c(-0.01, 1),
                           breaks = seq(0, 1, 0.25)) +
        scale_colour_solarized(guide = FALSE) +
        scale_fill_solarized(guide = FALSE) +
        geom_dl(method = list(dl.trans(x = x + 0.3), "last.qp", cex = 1,
                              fontfamily = font))
      if (input$mean) {
        g +
          geom_smooth(aes(linetype = type, weight = total), method = "loess",
                      se = FALSE, colour = "black", data = mean_data()) +
          geom_point(aes(shape = form), colour = "black", data = mean_data())
      } else {
        g
      }
    }
  }

  word_options <- reactive({
    if (length(input_forms()) == 1) {
      words <- names(filter(instrument_tables,
                            language == input_language(),
                            form == input_forms())$words_by_definition[[1]])
    } else {
      words1 <- names(filter(instrument_tables,
                             language == input_language(),
                             form == input_forms()[1])$words_by_definition[[1]])
      words2 <- names(filter(instrument_tables,
                             language == input_language(),
                             form == input_forms()[2])$words_by_definition[[1]])
      words <- intersect(words1, words2)
    }
  })

  observe({
    words <- word_options()
   updateSelectInput(session, "words", choices = words,
                     selected = if (length(words)) words[1] else "")
#    isolate({
#         select_words <- input_words()
#         select_words <- select_words[select_words %in% words]
#         updateSelectInput(session, "words", choices = words, selected = input_words())
#    })
  })

  forms <- reactive({
    valid_form <- function(form) {
      form %in% unique(filter(instrument_tables,
                              language == input_language())$form)
    }
    form_opts <- Filter(valid_form,
                        list("Words & Sentences" = "WS",
                             "Words & Gestures" = "WG"))
    if (all(c("WS", "WG") %in% form_opts)) {
      form_opts$"Both" <- "WG WS"
    }
    form_opts
  })

  measures <- reactive({
    if ("WG" %in% input_forms()) {
      list("Produces" = "produces", "Understands" = "understands")
    } else {
      list("Produces" = "produces")
    }
  })

  output$trajectory_plot <- renderPlot(trajectory_plot(), height = function() {
    session$clientData$output_trajectory_plot_width * 0.7
  })

  output$language_selector <- renderUI({
    selectInput("language", label = strong("Language"),
                choices = languages, selected = input_language())
  })

  output$form_selector <- renderUI({
    selectInput("form", label = strong("Form"),
                choices = forms(), selected = input_form())
  })

  output$measure_selector <- renderUI({
    selectInput("measure", label = strong("Measure"),
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

  table_data <- reactive({
    traj <- trajectory_data()
    if (nrow(traj) == 0) {
      expand.grid(age = age_min():age_max(), form = input_forms()) %>%
        select(form, age)
    } else {
      traj %>%
        select(form, age, item, prop) %>%
        spread(item, prop)
    }
  })

  output$table <- renderTable(table_data(),
                              include.rownames = FALSE, digits = 2)

  output$download_table <- downloadHandler(
    filename = function() "item_trajectory_table.csv",
    content = function(file) {
      td <- table_data()
      extra_cols <- data.frame(language = rep(input_language(), nrow(td)),
                               measure = rep(input_measure(), nrow(td)))
      write.csv(bind_cols(extra_cols, td), file, row.names = FALSE)
    })

  output$download_plot <- downloadHandler(
    filename = function() "item_trajectory.pdf",
    content = function(file) {
      cairo_pdf(file, width = 10, height = 7)
      print(trajectory_plot())
      dev.off()
    })

  output$loaded <- reactive(1)

})
