library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
source("../app_themes.R")
source("../data_loading.R")
Sys.setlocale(locale="en_US.UTF-8")

## DEBUGGING
#input <- list(language = "English", form = "WS", measure = "produces",
#            words = c("item_1"), wordform = NULL, complexity = NULL)


shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
  wordbank <- connect.to.wordbank("local")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables)
  
  items <- get.item.data(common.tables) %>%
    mutate(definition = iconv(definition, from = "utf8", to = "utf8"))
  
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
  
  tables <- get.instrument.tables(wordbank, common.tables)
  instrument.tables <- tables %>%
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
    left_join(tables)
  
  languages <- sort(unique(instrument.tables$language))
  
  start.language <- function() {"English"}
  start.form <- function() {"WS"}
  start.measure <- function() {"produces"}
  start.words <- function(words) {words[[1]]}
  start.wordform <- function(wordform) {}
  start.complexity <- function(complexity) {}
  
  data.fun <- function(instrument, input.form, input.measure,
                       input.words, input.wordform, input.complexity) {
    
    instrument.table <- instrument$table[[1]]
    
    if(!is.null(input.words)) {
      word.data <- get.instrument.data(instrument.table, input.words) %>%
        mutate(produces = value == 'produces',
               understands = value == 'understands' | value == 'produces') %>%
        select(-value) %>%
        gather(measure, value, produces, understands) %>%
        filter(measure == input.measure) %>%
        left_join(admins) %>%
        group_by(item.id, age) %>%
        summarise(score = mean(value, na.rm=TRUE)) %>%
        rowwise %>%
        mutate(item = instrument$words.by.id[[1]][[paste("item_", item.id, sep="")]],
               type = 'word')
    } else {word.data <- data.frame()}
    
    if(!is.null(input.wordform)) {
      wordform.data <- get.instrument.data(instrument.table, input.wordform) %>%
        mutate(produces = value == 'produces') %>%
        select(-value) %>%
        left_join(admins) %>%
        group_by(item.id, age) %>%
        summarise(score = mean(produces, na.rm=TRUE)) %>%
        rowwise %>%
        mutate(item = instrument$wordform.by.id[[1]][[paste("item_", item.id, sep="")]],
               type = 'wordform')
    } else {wordform.data <- data.frame()}
    
    if(!is.null(input.complexity)) {
      complexity.data <- get.instrument.data(instrument.table, input.complexity) %>%
        mutate(complex = value == 'complex') %>%
        select(-value) %>%
        left_join(admins) %>%
        group_by(item.id, age) %>%
        summarise(score = mean(complex, na.rm=TRUE)) %>%
        rowwise %>%
        mutate(item = instrument$complexity.by.id[[1]][[paste("item_", item.id, sep="")]],
               type = 'complexity')
    } else {complexity.data <- data.frame()}
    
    data <- bind_rows(word.data, wordform.data, complexity.data) %>%
      filter(age >= instrument$age_min & age <= instrument$age_max)
    
    return(data)
  }
  
  input.language <- reactive({
    ifelse(is.null(input$language), start.language(), input$language)
  })
  input.form <- reactive({
    ifelse(is.null(input$form), start.form(), input$form)
  })
  input.measure <- reactive({
    ifelse(is.null(input$measure), start.measure(), input$measure)
  })
  input.words <- reactive(input$words)
  input.wordform <- reactive(input$wordform)
  input.complexity <- reactive(input$complexity)
  
  instrument <- reactive({
    filter(instrument.tables, language == input.language(), form == input.form())
  })
  
  data <- reactive({
    data.fun(instrument(), input.form(), input.measure(),
             input.words(), input.wordform(), input.complexity())
  })
  
  ylabel <- reactive({
    if (input.measure() == "understands") {"Proportion of Children Understanding"}
    else if (input.measure() == "produces") {"Proportion of Children Producing"}
  })
  
  age.min <- reactive(instrument()$age_min)
  age.max <- reactive(instrument()$age_max)
  
  plot <- function() {
    data <- data()
    if (nrow(data) == 0) {
      ggplot(data) +
        geom_point() + 
        scale_x_continuous(name = "\nAge (months)",
                           breaks = age.min():age.max(),
                           limits = c(age.min(), age.max()+3)) +
        scale_y_continuous(name = paste(ylabel(), "\n", sep=""),
                           limits = c(-.01,1),
                           breaks = seq(0,1,.25)) +
        theme(text=element_text(family=font))
    } else {
      ggplot(data, aes(x=age, y=score, colour=item, label=item)) +
        geom_smooth(aes(linetype=type), se=FALSE, method="loess") +
        geom_point(aes(shape=type)) +
        scale_x_continuous(name = "\nAge (months)",
                           breaks = age.min():age.max(),
                           limits = c(age.min(), age.max()+3)) +
        scale_y_continuous(name = paste(ylabel(), "\n", sep=""),
                           limits = c(-.01,1),
                           breaks = seq(0,1,.25)) +
        scale_colour_brewer(palette=qual.palette) +
        geom_dl(method = list(dl.trans(x=x +.3), "last.qp", cex=1, fontfamily=font)) +
        theme(legend.position="none",
              text=element_text(family=font))
    }
  }
  
  observe({
    words <- filter(instrument.tables,
                    language == input.language(),
                    form == input.form())$words.by.definition[[1]]
    updateSelectInput(session, 'words', choices = words, selected = "")
  })
  
  observe({
    wordforms <- filter(instrument.tables,
                        language == input.language(),
                        form == input.form())$wordform.by.definition[[1]]
    updateSelectInput(session, 'wordform', choices = wordforms, selected = "")
  })
  
  observe({
    complexity <- filter(instrument.tables,
                         language == input.language(),
                         form == input.form())$complexity.by.definition[[1]]
    updateSelectInput(session, 'complexity', choices = complexity, selected = "")
  })
  
  forms <- reactive({
    Filter(function(form) {form %in% unique(filter(instrument.tables,
                                                   language == input.language())$form)},
           list("Words & Sentences" = "WS", "Words & Gestures" = "WG"))
  })
  
  measures <- reactive({
    if (input.form() == "WG") {
      list("Produces" = "produces", "Understands" = "understands")
    } else if (input.form() == "WS") {
      list("Produces" = "produces")
    }
  })
  
  output$plot <- renderPlot({
    plot()    
  }, height = function() {
    session$clientData$output_plot_width * 0.7
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
  
  #   output$words_selector <- renderUI({
  #     print(words())
  #     selectizeInput("words", label = h4("Words"), 
  #                    selected = start.words(names(instrument()$words.by.id[[1]])),
  #                    multiple = TRUE,
  #                    choices = words())  
  #   })
  
  #   output$wordform_selector <- renderUI({
  #     selectizeInput("wordform", label = h4("Word Forms"), 
  #                    choices = wordform(),
  #                    multiple = TRUE)
  #   })
  
  #   output$complexity_selector <- renderUI({
  #     selectizeInput("complexity", label = h4("Complexity Items"), 
  #                    choices = complexity(),
  #                    multiple = TRUE)
  #   })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'item_trajectory.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'item_trajectory.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
  output$loaded <- reactive({1})
  
})
