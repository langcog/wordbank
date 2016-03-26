library(shiny)
library(shinythemes)

shinyUI(fluidPage(

  theme = shinytheme("spacelab"),

  titlePanel("Administration Data"),
  br(),

  conditionalPanel(
    condition = "output.loaded != 1",
    h4("Loading...")
  ),

  conditionalPanel(
    condition = "output.loaded == 1",

    fluidRow(
      column(3, uiOutput("language_selector")),
      column(3, uiOutput("form_selector")),
      column(4, uiOutput("age_selector"))
    ),
    fluidRow(
      column(3, uiOutput("gender_selector")),
      column(3, uiOutput("momed_selector")),
      br(),
      column(5, downloadButton("download_data", "Download Data", class = "btn-xs"),
             align = "right")
    ),

    fluidRow(
      column(11, dataTableOutput(outputId = "table"))
    )
  )
))
