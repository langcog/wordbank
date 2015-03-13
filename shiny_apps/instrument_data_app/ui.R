library(shiny)
library(shinythemes)

shinyUI(fluidPage(theme = shinytheme("spacelab"),
  
  # Application title
  titlePanel("Instrument Data"),
  
  br(),
  
  sidebarLayout(
    
    sidebarPanel(width=3,
      uiOutput("language_selector"),
      uiOutput("form_selector"),
      submitButton("Get Data"),
      br(),br(),
      downloadButton('downloadData', 'Download Data')
      ),
    
    mainPanel(width=9,
      conditionalPanel(condition="$('html').attr('class') == 'shiny-busy'",
                       fluidRow(column(12, tags$h4("Loading data..."), align="center")),
                       fluidRow(column(12, imageOutput("loading"), align="center"))
      ),
      conditionalPanel(condition="$('html').attr('class') != 'shiny-busy'",
        dataTableOutput(outputId="table")
      )
    )
    
  )
))