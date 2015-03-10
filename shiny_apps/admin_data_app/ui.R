library(shiny)
library(shinythemes)

shinyUI(fluidPage(theme = shinytheme("spacelab"),
  
  # Application title
  titlePanel("Administration Data"),
  
  br(),
  
  fluidRow(
    column(4, uiOutput("language_selector")),
    column(4, uiOutput("form_selector")),
    column(4, uiOutput("age_selector"))
    ),
  fluidRow(
    column(4, uiOutput("sex_selector")),
    column(4, uiOutput("momed_selector"))
    ),
  
  fluidRow(
    dataTableOutput(outputId="table")
  )
))