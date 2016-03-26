library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  theme = shinytheme("spacelab"),

  titlePanel("Item Data"),
  br(),

  sidebarLayout(

    sidebarPanel(
      width = 3,

      conditionalPanel(
        condition = "output.loaded != 1",
        h4("Loading...")
      ),

      conditionalPanel(
        condition = "output.loaded == 1",

        uiOutput("language_selector"),
        uiOutput("form_selector"),
        uiOutput("measure_selector"),
        uiOutput("age_selector")
      )
    ),

    mainPanel(
      width = 9,
      tags$style(type = "text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      conditionalPanel(
        condition = "output.loaded == 1",
        downloadButton("download_all", "Download all pages",
                       class = "btn-default btn-xs"),
        downloadButton("download_current", "Download current page",
                       class = "btn-default btn-xs"),
        downloadButton("download_selected", "Download selected rows",
                       class = "btn-default btn-xs"),
        br(), br(),
        DT::dataTableOutput("table")
      )
    )

  )
))
