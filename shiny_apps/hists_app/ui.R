library(shiny)
library(shinythemes)

shinyUI(fluidPage(theme = shinytheme("spacelab"),
  
  # Application title
  titlePanel("Vocabulary Distribution"),
  
  br(),
    
  sidebarLayout(
    sidebarPanel(
      uiOutput("language_selector"),
      uiOutput("form_selector"),      
      uiOutput("measure_selector"),
      selectInput("qsize", label = h4("Quantile size"), 
                  choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                  selected = .2),
      uiOutput("age_selector"),
      br(),
      downloadButton('downloadPlot', 'Download Plot'),
      br(),br(),
      downloadButton('downloadData', 'Download Data'),
      width=3
      ),

    # Show a plot of the generated distribution
      mainPanel(
        tags$style(type="text/css",
                   ".shiny-output-error { visibility: hidden; }",
                   ".shiny-output-error:before { visibility: hidden; }"
        ),
        plotOutput("plot", width = "100%", height = "auto"),
        width=9
      )
    )
  ))