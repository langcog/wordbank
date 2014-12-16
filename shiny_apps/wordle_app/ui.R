library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Productive Vocabulary Word Clouds"),
  
  sidebarLayout(
    sidebarPanel(
      tags$head(tags$style(type="text/css", "
             #loadmessage {
                           position: fixed;
                           top: 0px;
                           left: 0px;
                           width: 100%;
                           padding: 5px 0px 5px 0px;
                           text-align: center;
                           font-weight: bold;
                           font-size: 100%;
                           color: #000000;
                           background-color: #CCFF66;
                           z-index: 105;
                           }")),
      selectInput("instrument", label = h4("Instrument"), 
                  choices = list("Words and Gestures" = "WG", 
                                 "Words and Sentences" = "WS"), 
                  selected = 1),
      uiOutput("age_selector_control"),
      sliderInput("freq", 
                  h4("Minimum Frequency"), 
                  min = 1,  max = 100, value = 10),
      sliderInput("max", 
                  h4("Maximum Number of Words"), 
                  min = 1,  max = 200,  value = 150)),
    
      # Show a plot of the generated distribution
      mainPanel(
        tags$style(type="text/css",
                   ".shiny-output-error { visibility: hidden; }",
                   ".shiny-output-error:before { visibility: hidden; }"
        ),
        plotOutput("plot")
      )
    )
  ))