library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  titlePanel("Vocabulary Distribution"),
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
        selectInput("bin_size", label = h4("Bin size"), 
                    choices = list("10 words" = 10, "20 words" = 20,
                                   "50 words" = 50, "100 words" = 100),
                    selected = 20),
        uiOutput("age_selector"),
        br(),
        downloadButton('downloadPlot', 'Download Plot'),
        br(),br(),
        downloadButton('downloadData', 'Download Data')
      )),
    
    mainPanel(
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"
      ),
      plotOutput("plot", width = "100%", height = "auto"),
      h5(textOutput("sample_size_header")),
      tableOutput("sample_size"),      
      width=9
    )
  )
))