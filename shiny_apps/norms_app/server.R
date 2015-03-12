############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
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

# wordbank <- src_mysql(dbname="wordbank")
wordbank <- src_mysql(dbname="wordbank", host="54.200.225.86",
                      user="wordbank", password="wordbank")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables$momed,
                                  common.tables$child,
                                  common.tables$instrumentsmap,
                                  common.tables$administration) %>%
  gather(measure, vocab, comprehension, production)

instrument.tables <- get.instrument.tables(wordbank, common.tables$instrumentsmap)
languages <- unique(instrument.tables$language)

plot.attr.fun <- function(form, measure) {
  plot.attr = list()
  if(form == "WG") {
    if(measure == "comprehension") {
      plot.attr$ylabel <- "Size of Receptive Vocabulary"
    } else {
      plot.attr$ylabel <- "Size of Productive Vocabulary" 
    }
    plot.attr$xlims = c(8,18)
    plot.attr$xbreaks = 8:18
  } else {
    plot.attr$ylabel = "Size of Productive Vocabulary"
    plot.attr$xlims = c(16,30)
    plot.attr$xbreaks = 16:30
  }
  return(plot.attr)
}

measure.fun <- function(input.form) {
  if (input.form == "WG") {
    measures <- list("Produces" = "production", "Understands" = "comprehension")
  } else if (input.form == "WS") {
    measures <- list("Produces" = "production")
  }
  return(measures)
}

start.language <- function(language) {
  ifelse(is.null(language), "English", language)
}

start.form <- function(form) {
  ifelse(is.null(form), "WS", form)
}

start.measure <- function(measure) {
  ifelse(is.null(measure), "production", measure)
}

start.demo <- function(demo) {
  ifelse(is.null(demo), "identity", demo)
}

## DEBUGGING
# input <- list(language = "English", form = "WS", measure = "production", qsize = ".2", demo = "birth.order")
possible_demo_fields <- list("None" = "identity", 
                             "Birth order" = "birth.order", 
                             "Ethnicity" = "ethnicity",
                             "Sex" = "sex",
                             "Mother's education" = "momed.level")
admins$identity <- "all data"
min_obs <- 100

############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
shinyServer(function(input, output, session) {
  
  cuts <- reactive({
    seq(0.0, 1.0, by=as.numeric(input$qsize))
  })
  
  middles <- reactive({
    cuts()[2:length(cuts())] - as.numeric(input$qsize)/2
  })
  
  groups_with_data <- reactive({
    admins %>% 
      filter(language == start.language(input$language),
             form == start.form(input$form),
             measure == start.measure(input$measure)) %>%
      group_by_(input$demo) %>%
      summarise(n = n()) %>%
      filter_(interp("!is.na(x)", x = as.name(input$demo))) %>%
              filter(n > min_obs)
  })
  
  data <- reactive({
    admins %>% 
      filter(language == start.language(input$language),
                      form == start.form(input$form),
                      measure == start.measure(input$measure)) %>%
      right_join(groups_with_data()) %>%
      group_by_("age", input$demo) %>%
      filter_(interp("!is.na(x)", x = as.name(input$demo))) %>%
      mutate(percentile = rank(vocab) / length(vocab),
             quantile = cut(percentile,
                            breaks=cuts(), 
                            labels=middles()))
  })
  
  plot.attr <- reactive({plot.attr.fun(start.form(input$form),
                                       start.measure(input$measure))})
  
  curves <- reactive({
    crs <- admins %>% 
      filter(language == start.language(input$language),
                      form == start.form(input$form),
                      measure == start.measure(input$measure)) %>%
      right_join(groups_with_data()) %>%
      group_by_(input$demo) %>%
      filter_(interp("!is.na(x)", x = as.name(input$demo))) %>% # no NAs
      do(mod = gather(data.frame(predictQR(gcrq(vocab ~ ps(age, 
                                                           monotone=1, 
                                                           lambda=60), 
                                         data = ., 
                                         tau = middles()), 
                              newdata = data.frame(age = plot.attr()$xlims[1]:plot.attr()$xlims[2]))), 
                      quantile, prediction)$prediction) %>% 
      unnest(mod) %>%
      group_by_(input$demo) %>%
      do(bind_cols(.,
                   expand.grid(age = plot.attr()$xlims[1]:plot.attr()$xlims[2], 
                               quantile = middles())))
  })
    
  plot <- function() {
    ggplot(data(), aes(x=age, y=vocab, colour=quantile)) + 
      geom_jitter(width=.1) +
      facet_wrap(input$demo) + 
      geom_line(data = curves(), 
                aes(x = age, 
                    y = mod, 
                    group = factor(quantile),
                    colour = factor(quantile)),
                size = 1) + 
      scale_x_continuous(name="\nAge (months)",
                         breaks=plot.attr()$xbreaks,
                         limits=plot.attr()$xlims) +
      ylab(paste(plot.attr()$ylabel, "\n", sep="")) +
      scale_colour_brewer(name="Quantile\nMidpoint",
                          palette=seq.palette) +
      theme(text=element_text(family=font))
  }
  
  forms <- reactive({unique(filter(instrument.tables,
                                   language == start.language(input$language))$form)})
  
  measures <- reactive({measure.fun(start.form(input$form))})
  
  demos <- reactive({
    demo_fields <- possible_demo_fields
#     for (i in seq(length(possible_demo_fields),1,-1)) {
#       if (all(is.na(data()[possible_demo_fields[[i]]]))) {
#         demo_fields <- demo_fields[-i]
#       }
#     }
    return(demo_fields)
  })                            
  
  output$plot <- renderPlot({
    plot()
  }, height = function() {
    session$clientData$output_plot_width * 0.7
  })
  
  ### FIELD SELECTORS
  output$language_selector <- renderUI({    
    selectizeInput("language", label = h5("Language"), 
                   choices = languages, selected = start.language(NULL))
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = h5("Form"), 
                   choices = forms(), selected = start.form(NULL))
  })
  
  output$measure_selector <- renderUI({
    selectizeInput("measure", label = h5("Measure"), 
                   choices = measures(), selected = start.measure(NULL))
  })
  
  output$demo_selector <- renderUI({
    selectizeInput("demo", label = h5("Demographic Split Variable"), 
                   choices = demos(), selected = start.demo(NULL))
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'vocabulary_norms.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$downloadPlot <- downloadHandler(
    filename = function() { 'vocabulary_norms.pdf' },
    content = function(file) {
      cairo_pdf(file, width=10, height=7, family=font)
      print(plot())
      dev.off()
    })
  
  # output$downloadReport <- downloadHandler(
  #   filename = function() { 'vocabulary_norms_report.pdf' },
  #   
  #   content = function(file) {
  #     library(rmarkdown)
  #     out <- render('report.Rmd', pdf_document())
  #     file.rename(out, file)
  #   })
  
})
