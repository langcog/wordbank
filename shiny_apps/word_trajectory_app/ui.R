library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Individual Word Trajectories"),
  
  sidebarLayout(
    sidebarPanel(
      uiOutput("language_selector"),
      uiOutput("form_selector"),      
      uiOutput("measure_selector"),
      uiOutput("words_selector")),
    
    # Show a plot of the generated distribution
    mainPanel(
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"
      ),
      plotOutput("plot", width = "100%", height = "auto")
    )
  )
))