library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Norms"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("instrument", label = h3("Instrument"), 
                  choices = list("Words and Gestures" = "WG", "Words and Sentences" = "WS"), 
                  selected = 1),
      selectInput("measure", label = h3("Measure"), 
                  choices = list("Understands" = "understands", "Produces" = "produces"), 
                  selected = 1),
      selectInput("lang", label = h3("Language"), 
                  choices = list("English" = 1), 
                  selected = 1),
      selectInput("qsize", label = h3("Quantile size"), 
                  choices = list("10%" = .1, 
                                 "20%" = .2, "25%" = .25, 
                                 "33%" = .33),
                  selected = 1)),

    # Show a plot of the generated distribution
      mainPanel(
        plotOutput("plot")
      )
    )
  ))