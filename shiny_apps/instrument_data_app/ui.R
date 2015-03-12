library(shiny)
library(shinythemes)

shinyUI(fluidPage(theme = shinytheme("spacelab"),
  
  # Application title
  titlePanel("Instrument Data"),
  
  br(),
  
  sidebarLayout(
    
    sidebarPanel(
      uiOutput("language_selector"),
      uiOutput("form_selector"),
      br(),
      downloadButton('downloadData', 'Download Data'),
      width=3
      ),
    
    mainPanel(
      dataTableOutput(outputId="table"),
      width=9
    )
    
  )
))