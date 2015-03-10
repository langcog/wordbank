############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(magrittr)
library(tidyr)
library(dplyr)
library(ggplot2)
library(directlabels)
library(RMySQL)
source("../app_themes.R")
source("../data_loading.R")
Sys.setlocale(locale="C")

wordbank <- src_mysql(dbname="wordbank")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables$momed,
                                  common.tables$child,
                                  common.tables$instrumentsmap,
                                  common.tables$administration)

items <- get.item.data(common.tables$wordmapping,
                       common.tables$instrumentsmap)

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

tables <- get.instrument.tables(wordbank, common.tables$instrumentsmap)
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

languages <- unique(instrument.tables$language)

start.language <- function() {"English"}
start.form <- function() {"WS"}
start.measure <- function() {"produces"}
start.words <- function(words) {words[[1]]}
start.wordform <- function(wordform) {}
start.complexity <- function(complexity) {}

# start.words <- function(words, instrument.words) {
#   if(is.null(words)) {c("item_100")} else {words}
# }


data.fun <- function(input.language, input.form, input.measure,
                     input.words, input.wordform, input.complexity) {
  
  instrument <- filter(instrument.tables, language == input.language, form == input.form)
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
  
  data <- bind_rows(word.data, wordform.data, complexity.data)
  
  if (input.form == "WS") {
    data %<>% filter(age >= 16 & age <= 30)
  } else if (input.form == "WG") {
    data %<>% filter(age >= 8 & age <= 18)      
  }
  return(data)
}

plot.attr.fun <- function(input.form, input.measure) {
  plot.attr = list()
  if (input.form == "WG") {
    plot.attr$xlims = c(8,20)
    plot.attr$xbreaks = 8:18
    if (input.measure == "understands") {
      plot.attr$ylabel <- "Proportion of Children Understanding"
    } else if (input.measure == "produces") {
      plot.attr$ylabel <- "Proportion of Children Producing" 
    }
  } else if (input.form == "WS") {
    plot.attr$xlims = c(16,35)
    plot.attr$xbreaks = 16:30
    plot.attr$ylabel = "Proportion of Children Producing"
  }
  return(plot.attr)
}

## DEBUGGING
#input <- list(language = "Danish", form = "WS", measure = "produces",
#              words = c("item_1"))
#instrument <- function(){filter(instrument.tables,
#                               language == start.language(input$language),
#                               form == start.form(input$form))}
#plot.words <- function(){if(is.null(input$words)) {c("item_100")} else {input$words}}
#data <- function(){data.fun(start.language(input$language),
#                           start.form(input$form),
#                           start.measure(input$measure),
#                           plot.words())}
#plot.attr <- function(){plot.attr.fun(start.form(input$form),
#                                     start.measure(input$measure))}

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output, session) {
  
  input.language <- reactive({ifelse(is.null(input$language),
                               start.language(), input$language)})
  input.form <- reactive({ifelse(is.null(input$form),
                           start.form(), input$form)})
  input.measure <- reactive({ifelse(is.null(input$measure),
                           start.measure(), input$measure)})
#  input.words <- reactive({
#    if(is.null(input$words)) {start.words(names(instrument()$words.by.id[[1]]))}
#    else {input$words}
#    })
  input.words <- reactive(input$words)
#  input.wordform <- reactive({
#    if(is.null(input$wordform)) {start.wordform(names(instrument()$wordform.by.id[[1]]))}
#    else {input$wordform}
#  })
  input.wordform <- reactive(input$wordform)
#  input.complexity <- reactive({
#    if(is.null(input$complexity)) {start.complexity(names(instrument()$complexity.by.id[[1]]))}
#    else {input$complexity}
#  })
  input.complexity <- reactive(input$complexity)

  instrument <- reactive({filter(instrument.tables,
                                 language == input.language(),
                                 form == input.form())})

  data <- reactive({data.fun(input.language(), input.form(), input.measure(),
                             input.words(), input.wordform(), input.complexity())})

  plot.attr <- reactive({plot.attr.fun(input.form(), input.measure())})

  plot <- function() {
    ggplot(data(), aes(x=age, y=score, colour=item, label=item)) +
      geom_smooth(aes(linetype=type), se=FALSE, method="loess") +
      geom_point(aes(shape=type)) +
      scale_x_continuous(name = "\nAge (months)",
                         breaks = plot.attr()$xbreaks,
                         limits = plot.attr()$xlims) +
      scale_y_continuous(name = paste(plot.attr()$ylabel, "\n", sep=""),
                         limits = c(-.01,1),
                         breaks = seq(0,1,.25)) +
      scale_colour_brewer(palette=qual.palette) +
      geom_dl(method = list(dl.trans(x=x +.3), "last.qp", cex=1, fontfamily=font)) +
      theme(legend.position="none",
            text=element_text(family=font))
  }
  
  words <- reactive({filter(instrument.tables,
                            language == input.language(),
                            form == input.form())$words.by.definition[[1]]})
  wordform <- reactive({filter(instrument.tables,
                               language == input.language(),
                               form == input.form())$wordform.by.definition[[1]]})
  complexity <- reactive({filter(instrument.tables,
                                 language == input.language(),
                                 form == input.form())$complexity.by.definition[[1]]})
    
  forms <- reactive({unique(filter(instrument.tables,
                                   language == input.language())$form)})
  measures <- reactive({
    if (input.form() == "WG") {
      list("Produces" = "produces", "Understands" = "understands")
    } else if (input.form() == "WS") {
      list("Produces" = "produces")
    }
  })
  
  ### PLOT RENDERER
  output$plot <- renderPlot({
    plot()    
  }, height = function() {
    session$clientData$output_plot_width * 0.7
  })  
  
  ### FIELD SELECTORS
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
  
  output$words_selector <- renderUI({
    selectizeInput("words", label = h4("Words"), 
                   choices = words(),
                   selected = start.words(names(instrument()$words.by.id[[1]])),
                   multiple = TRUE)
  })

  output$wordform_selector <- renderUI({
    selectizeInput("wordform", label = h4("Wordform Items"), 
                   choices = wordform(),
#                   selected = start.wordform(names(instrument()$wordform.by.id[[1]])),
                   multiple = TRUE)
  })
  
  output$complexity_selector <- renderUI({
    selectizeInput("complexity", label = h4("Complexity Items"), 
                   choices = complexity(),
#                   selected = start.complexity(names(instrument()$complexity.by.id[[1]])),
                   multiple = TRUE)
  })
  
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
  
})
