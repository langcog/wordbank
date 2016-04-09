library(shiny)
library(shinythemes)
library(DT)


shinyUI(fluidPage(
  theme = shinytheme("spacelab"),

  titlePanel("Full Child-by-Word Data"),
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
        br(),
        actionButton("get_data", "Get Data"),
        p("Caution: can take a while")
      )),

    mainPanel(
      width = 9,
      conditionalPanel(
        condition = "$('html').attr('class') == 'shiny-busy'",
        fluidRow(column(12, tags$h4("Please wait..."),
                        align = "center")),
        fluidRow(column(12, imageOutput("loading"),
                        align = "center"))
      ),
      conditionalPanel(
        condition = "$('html').attr('class') != 'shiny-busy'",
        uiOutput("download_button"),
        br(),
        DT::dataTableOutput(outputId = "table")
      )
    )

  )
))
