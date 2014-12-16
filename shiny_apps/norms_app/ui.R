library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Norms"),
  
  
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
                  choices = list("Words and Gestures" = "WG", "Words and Sentences" = "WS"), 
                  selected = 1),
      uiOutput("field_selector_control"),
#       selectInput("measure", label = h4("Measure"), 
#                   choices = list("Understands" = "understands", "Produces" = "produces"), 
#                   selected = 1),
      selectInput("lang", label = h4("Language"), 
                  choices = list("English" = 1), 
                  selected = 1),
      selectInput("qsize", label = h4("Quantile size"), 
                  choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                  selected = 1)),

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