library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  theme = shinytheme("spacelab"),
  
  titlePanel("Item Data"),  
  br(),
  
  sidebarLayout(
    
    sidebarPanel(
      width=3,
      
      conditionalPanel(
        condition="output.loaded != 1",
        h4("Loading...")
      ),
      
      conditionalPanel(
        condition="output.loaded == 1",
        
        uiOutput("language_selector"),
        uiOutput("form_selector"),
        uiOutput("measure_selector"),
        uiOutput("age_selector"),
        br(), br(),
        downloadButton('downloadAll', 'Download all pages', class = "btn-primary btn-sm"),
        br(), br(),
        downloadButton('downloadCurrent', 'Download current page', class = "btn-primary btn-sm"),
        br(), br(),
        downloadButton('downloadSelected', 'Download selected rows', class = "btn-primary btn-sm")
      )
    ),
    
    mainPanel(
      width=9,
      tags$style(type = "text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),      
      conditionalPanel(
        condition="output.loaded == 1",
#     conditionalPanel(condition="$('html').attr('class') == 'shiny-busy'",
#                      fluidRow(column(12, tags$h4("Please wait..."), align="center")),
#                      fluidRow(column(12, imageOutput("loading"), align="center"))
#     ),
#     conditionalPanel(condition="$('html').attr('class') != 'shiny-busy'",
                       DT::dataTableOutput('table')
#      )
        )
      )
    
  )
))