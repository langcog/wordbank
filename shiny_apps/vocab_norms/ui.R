library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  titlePanel("Vocabulary Norms"),
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
        uiOutput("demo_selector"),
        selectInput("qsize", label = h4("Quantile size"), 
                    choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                    selected = .2),
        br(),
        downloadButton('downloadPlot', 'Download Plot'),
        br(),br(),
        downloadButton('downloadData', 'Download Data')
      )),
    
    mainPanel(
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      plotOutput("plot", width = "100%", height = "auto"),
      width=9)
  )
))