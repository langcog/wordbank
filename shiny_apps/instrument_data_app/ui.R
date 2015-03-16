library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  theme = shinytheme("spacelab"),
  
  titlePanel("Instrument Data"),  
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
        
        actionButton("get_data", "Get Data"),
        p("Caution: takes a while"),
        uiOutput("language_selector"),
        uiOutput("form_selector"),
        br(), br(),
        downloadButton('downloadData', 'Download Data')
      )),
    
    mainPanel(
      width=9,
      conditionalPanel(condition="$('html').attr('class') == 'shiny-busy'",
                       fluidRow(column(12, tags$h4("Please wait..."), align="center")),
                       fluidRow(column(12, imageOutput("loading"), align="center"))
      ),
      conditionalPanel(condition="$('html').attr('class') != 'shiny-busy'",
                       dataTableOutput(outputId="table")
      )
    )
    
  )
))