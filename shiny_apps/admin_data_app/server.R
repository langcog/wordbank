library(shiny)
library(RMySQL)
library(dplyr)
library(magrittr)
source("../data_loading.R")

## DEBUGGING
#input <- list(language = "English", form = "WS", age = c(18,30))

shinyServer(function(input, output, session) {
  
  output$loaded <- reactive({0})
  outputOptions(output, 'loaded', suspendWhenHidden=FALSE)
  
  wordbank <- src_mysql(dbname = "wordbank", user = "wordbank",
                        password = "wordbank")
  
  common.tables <- get.common.tables(wordbank)
  
  admins <- get.administration.data(common.tables$momed,
                                    common.tables$child,
                                    common.tables$instrumentsmap,
                                    common.tables$administration) %>%
    select(data_id, language, form, age, sex, momed.level, comprehension, production) %>%
    rename(momed = momed.level) %>%
    mutate(sex = factor(sex, levels=c("F", "M"), labels=c("Female", "Male")),
           form = factor(form, levels=c("WG", "WS"), labels=c("Words & Gestures", "Words & Sentences")))
  
  
  input.language <- reactive({
    ifelse(is.null(input$language), "All", input$language)
  })
  
  input.form <- reactive({
    ifelse(is.null(input$form), "All", input$form)
  })
  
  input.sex <- reactive({
    ifelse(is.null(input$sex), "All", input$sex)
  })
  
  input.momed <- reactive({
    ifelse(is.null(input$momed), "All", input$momed)
  })
  
  input.age <- reactive({
    if(is.null(input$age)){c(min(admins$age), max(admins$age))} else {input$age}
  })
  
  data <- reactive({
    filter.data <- admins
    if (input.language() != "All"){
      filter.data %<>% filter(language == input.language())
    }
    if (input.form() != "All"){
      filter.data %<>% filter(form == input.form())
    }
    if (input.sex() != "All"){
      filter.data %<>% filter(sex == input.sex())
    }
    if (input.momed() != "All"){
      filter.data %<>% filter(momed == input.momed())
    }
    filter.data %<>% filter(age >= input.age()[[1]], age <= input.age()[[2]])
    filter.data
  })
  
  output$table <- renderDataTable({
    data()
  }, options = list(orderClasses = TRUE))
  
  output$language_selector <- renderUI({    
    selectizeInput("language", label = "Language:",
                   choices = c("All", unique(admins$language)),
                   selected = "All")
  })
  
  output$form_selector <- renderUI({    
    selectizeInput("form", label = "Form:",
                   choices = c("All", levels(unique(admins$form))),
                   selected = "All")
  })
  
  output$age_selector <- renderUI({
    sliderInput("age", label = "Age (Months):",
                min = min(admins$age), max = max(admins$age), step = 1,
                value = c(min(admins$age), max(admins$age)))
  })
  
  output$sex_selector <- renderUI({    
    selectizeInput("sex", label = "Sex:",
                   choices = c("All", levels(unique(admins$sex))),
                   selected = "All")
  })
  
  output$momed_selector <- renderUI({    
    selectizeInput("momed", label = "Maternal Education:",
                   choices = c("All", levels(unique(admins$momed))),
                   selected = "All")
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 'administration_data.csv' },
    content = function(file) {
      write.csv(data(), file)
    })
  
  output$loaded <- reactive({1})
  
})
