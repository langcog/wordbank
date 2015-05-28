library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
source("../app_themes.R")
source("../data_loading.R")
source("../palette.R")
Sys.setlocale(locale="en_US.UTF-8")
options(error = NULL)

## DEBUGGING
# input <- list(language = "English", form = "WG WS", measure = "produces",
#             words = c(), wordform = NULL, complexity = NULL)

list.items.by.definition <- function(item.data) {
  items <- item.data$item.id
  names(items) <- item.data$definition
  return(items)
}

list.items.by.id <- function(item.data) {
  items <- item.data$definition
  names(items) <- item.data$item.id
  return(items)
}

data.fun <- function(admins, fun.instrument, fun.measure, fun.words) {#, wordform, complexity) {

  instrument.word.data <- function(inst_id) {
    inst <- filter(fun.instrument, instrument_id == inst_id)
    word_ids <- inst$words.by.definition[[1]][fun.words]
    get.instrument.data(inst$table[[1]], word_ids[!is.na(word_ids)]) %>%
      mutate(instrument_id = inst$instrument_id)
  }

  if(!is.null(fun.words)) {
    word.data <- bind_rows(sapply(fun.instrument$instrument_id, instrument.word.data, simplify = FALSE)) %>% 
      mutate(produces = value == 'produces',
             understands = value == 'understands' | value == 'produces') %>%
      select(-value) %>%
      gather(measure, value, produces, understands) %>%
      filter(measure == fun.measure) %>%
      left_join(admins) %>%
      filter(!is.na(age)) %>%
      group_by(instrument_id, item.id, age) %>%
      summarise(mean = mean(value, na.rm = TRUE)) %>%
      group_by(instrument_id) %>%
      mutate(item.id = paste("item_", item.id, sep = "")) %>%
      rowwise() %>%
      mutate(item = filter(fun.instrument,
                           fun.instrument$instrument_id == instrument_id)$words.by.id[[1]][item.id],
             type = "word") %>%
      left_join(select(fun.instrument, instrument_id, form)) %>%
      select(-instrument_id, -item.id)
  } else {word.data <- data.frame()}
  
#   if(!is.null(input.wordform)) {
#     wordform.data <- get.instrument.data(instrument.table, input.wordform) %>%
#       mutate(produces = value == 'produces') %>%
#       select(-value) %>%
#       left_join(admins) %>%
#       group_by(item.id, age) %>%
#       summarise(score = mean(produces, na.rm=TRUE)) %>%
#       rowwise %>%
#       mutate(item = instrument$wordform.by.id[[1]][[paste("item_", item.id, sep="")]],
#              type = 'wordform')
#   } else {wordform.data <- data.frame()}
#   
#   if(!is.null(input.complexity)) {
#     complexity.data <- get.instrument.data(instrument.table, input.complexity) %>%
#       mutate(complex = value == 'complex') %>%
#       select(-value) %>%
#       left_join(admins) %>%
#       group_by(item.id, age, form) %>%
#       summarise(score = mean(complex, na.rm=TRUE)) %>%
#       rowwise %>%
#       mutate(item = instrument$complexity.by.id[[1]][[paste("item_", item.id, sep="")]],
#              type = 'complexity')
#   } else {complexity.data <- data.frame()}
 
  word.data
#  bind_rows(word.data, wordform.data, complexity.data)
}


##### SERVER STARTS HERE
shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
  wordbank <- connect.to.wordbank("dev")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables)
  
  items <- get.item.data(common.tables) %>%
    mutate(definition = iconv(definition, from = "utf8", to = "utf8"))
  
  start.instrument.tables <- init.instrument.tables(wordbank, common.tables)
  
  instrument.tables <- start.instrument.tables %>%
    group_by(instrument_id) %>%
    do(words.by.definition = list.items.by.definition(filter(items,
                                                             instrument_id==.$instrument_id,
                                                             type=='word')),
       words.by.id = list.items.by.id(filter(items,
                                             instrument_id==.$instrument_id,
                                             type=='word')),
       wordform.by.definition = list.items.by.definition(filter(items,
                                                                instrument_id==.$instrument_id,
                                                                type=='word_form')),
       wordform.by.id = list.items.by.id(filter(items,
                                                instrument_id==.$instrument_id,
                                                type=='word_form')),
       complexity.by.definition = list.items.by.definition(filter(items,
                                                                  instrument_id==.$instrument_id,
                                                                  type=='complexity')),
       complexity.by.id = list.items.by.id(filter(items,
                                                  instrument_id==.$instrument_id,
                                                  type=='complexity'))) %>%
    left_join(start.instrument.tables)
  
  languages <- sort(unique(instrument.tables$language))
  
  start.language <- function() {"English"}
  start.form <- function() {"WS"}
  start.measure <- function() {"produces"}
  start.words <- function(words) {words[[1]]}
  start.wordform <- function(wordform) {}
  start.complexity <- function(complexity) {}
  
  input.language <- reactive({
    ifelse(is.null(input$language), start.language(), input$language)
  })
  
  input.form <- reactive({
    #if (is.null(input$form)) start.form() else strsplit(input$form, ' ')[[1]]
    ifelse(is.null(input$form), start.form(), input$form)  
  })

  input.forms <- reactive({
    strsplit(input.form(), ' ')[[1]]
  })
  
  input.measure <- reactive({
    ifelse(is.null(input$measure), start.measure(), input$measure)
  })
  
  input.words <- reactive(input$words)
  input.wordform <- reactive(input$wordform)
  input.complexity <- reactive(input$complexity)
  
  instrument <- reactive({
    inst <- filter(instrument.tables, language == input.language(), form %in% input.forms())$instrument_id
    for (inst_id in inst) {
      if (length(instrument.tables[instrument.tables$instrument_id == inst_id, ]$table[[1]]) == 0) {
        instrument.tables <- add.instrument.table(wordbank, instrument.tables, inst_id)
      }
    }
    filter(instrument.tables, language == input.language(), form %in% input.forms())
  })
  
  data <- reactive({
    data.fun(admins, instrument(), input.measure(), input.words())
  })
  
  ylabel <- reactive({
    if (input.measure() == "understands") {"Proportion of Children Understanding"}
    else if (input.measure() == "produces") {"Proportion of Children Producing"}
  })
  
  age.min <- reactive({min(instrument()$age_min)})
  age.max <- reactive({max(instrument()$age_max)})
  
  plot <- function() {
    d <- data()
    if (nrow(d) == 0) {
      ggplot(d) +
        geom_point() + 
        scale_x_continuous(name = "\nAge (months)",
                           breaks = age.min():age.max(),
                           limits = c(age.min(), age.max() + 3)) +
        scale_y_continuous(name = paste(ylabel(), "\n", sep = ""),
                           limits = c(-0.01, 1),
                           breaks = seq(0, 1, 0.25)) +
        theme(text = element_text(family = font))
    } else {
      ggplot(d, aes(x = age, y = mean, colour = item, label = item)) +
        geom_smooth(aes(linetype = type), se = FALSE, method = "loess") +
        geom_point(aes(shape = form)) +
        scale_shape_manual(values = c(1, 20)) +
        scale_linetype_discrete(guide = FALSE) +
        scale_x_continuous(name = "\nAge (months)",
                           breaks = age.min():age.max(),
                           limits = c(age.min(), age.max() + 3)) +
        scale_y_continuous(name = paste(ylabel(), "\n", sep = ""),
                           limits = c(-0.01, 1),
                           breaks = seq(0, 1, 0.25)) +
        scale_color_manual(values = color_palette(length(unique(d$item))),
                           guide = FALSE) +
        geom_dl(method = list(dl.trans(x = x + 0.3), "last.qp", cex = 1, fontfamily = font)) +
        theme(legend.position = "right",
              text = element_text(family = font))
    }
  }
  
  observe({
    if (length(input.forms()) == 1) {
      words <- names(filter(instrument.tables,
                            language == input.language(),
                            form == input.forms())$words.by.definition[[1]])
    } else {
      words1 <- names(filter(instrument.tables,
                             language == input.language(),
                             form == input.forms()[1])$words.by.definition[[1]])
      words2 <- names(filter(instrument.tables,
                             language == input.language(),
                             form == input.forms()[2])$words.by.definition[[1]])
      words <- intersect(words1, words2)
    }
    updateSelectInput(session, 'words', choices = words, selected = "")
  })
  
#  observe({
#     wordforms <- filter(instrument.tables,
#                         language == input.language(),
#                         form == input.form())$wordform.by.definition[[1]]
#     updateSelectInput(session, 'wordform', choices = wordforms, selected = "")
#  })
  
#  observe({
#     complexity <- filter(instrument.tables,
#                          language == input.language(),
#                          form == input.form())$complexity.by.definition[[1]]
#     updateSelectInput(session, 'complexity', choices = complexity, selected = "")
#  })
  
  forms <- reactive({
    form_opts <- Filter(function(form) {form %in% unique(filter(instrument.tables,
                                                   language == input.language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
    
    if (all(c("WS", "WG") %in% form_opts)) {
      form_opts$"Both" <- "WG WS"
    }
    
    form_opts
  })
  
  measures <- reactive({
    if ("WG" %in% input.forms()) {
      list("Produces" = "produces", "Understands" = "understands")
    } else {
      list("Produces" = "produces")
    } 
  })
  
  output$plot <- renderPlot({
    plot()    
  }, height = function() {
    session$clientData$output_plot_width * 0.7
  })  
  
  output$language_selector <- renderUI({    
    selectInput("language", label = h4("Language"), 
                choices = languages, selected = input.language())
  })
  
  output$form_selector <- renderUI({    
    selectInput("form", label = h4("Form"),
                choices = forms(), selected = input.form())
  })
  
  output$measure_selector <- renderUI({
    selectInput("measure", label = h4("Measure"), 
                choices = measures(), selected = input.measure())
  })
  
  table.data <- reactive({
    d <- data()
    if (nrow(d) == 0) {
      expand.grid(age = age.min():age.max(), form = input.forms()) %>%
        select(form, age)
    } else {
      d %>%
        select(form, age, item, mean) %>%
        spread(item, mean)
    }
  })
  
  output$table <- renderTable({
    table.data()
  }, include.rownames = FALSE, digits = 2)

  output$downloadTable <- downloadHandler(
    filename = function() { 'item_trajectory_table.csv' },
    content = function(file) {
      td <- table.data()
      extra.cols <- data.frame(language = rep(input.language(), nrow(td)),
                               measure = rep(input.measure(), nrow(td)))
      write.csv(bind_cols(extra.cols, td), file, row.names = FALSE)
      })

#   output$downloadData <- downloadHandler(
#     filename = function() { 'item_trajectory_data.csv' },
#     content = function(file) {
#       write.csv(data(), file, row.names = FALSE)
#     })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'item_trajectory.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
  output$loaded <- reactive({1})
  
})
