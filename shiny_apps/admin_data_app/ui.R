library(shiny)
library(shinythemes)

shinyUI(fluidPage(theme = shinytheme("spacelab"),
  
  # Application title
  titlePanel("Administration Data"),
  
  br(),
  
  fluidRow(
    column(3, uiOutput("language_selector")),
    column(3, uiOutput("form_selector")),
    column(4, uiOutput("age_selector"))
    ),
  fluidRow(align="top",
    column(3, uiOutput("sex_selector")),
    column(3, uiOutput("momed_selector")),
    br(),
    column(5, downloadButton('downloadData', 'Download Data'), align="right")
    ),
  
  fluidRow(
    column(11, dataTableOutput(outputId="table"))
  )
))
