library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Norms"),
  
  sidebarLayout(
    sidebarPanel(
      uiOutput("language_selector"),
      uiOutput("form_selector"),      
      uiOutput("measure_selector"),
      selectInput("qsize", label = h4("Quantile size"), 
                  choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                  selected = .2),
      br(),
      downloadButton('downloadPlot', 'Download Plot'),
      br(),br(),
      downloadButton('downloadData', 'Download Data'),
#      downloadButton('downloadReport', 'Download Report'),
      width=3),
        
    # Show a plot of the generated distribution
    mainPanel(
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      plotOutput("plot", width = "100%", height = "auto"),
      width=9)
  )
))