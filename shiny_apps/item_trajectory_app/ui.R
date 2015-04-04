library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  titlePanel("Item Trajectories"),  
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
        selectizeInput("words", label = h4("Words"),
                       choices = NULL, multiple = TRUE),
        selectizeInput("wordform", label = h4("Wordforms"),
                       choices = NULL, multiple = TRUE),
        selectizeInput("complexity", label = h4("Complexity"),
                       choices = NULL, multiple = TRUE),
        #uiOutput("words_selector"),
        #uiOutput("wordform_selector"),
        #uiOutput("complexity_selector"),
        br(),
        downloadButton('downloadPlot', 'Download Plot'),
        br(),br(),
        downloadButton('downloadData', 'Download Data'),
        width=3)),
    
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