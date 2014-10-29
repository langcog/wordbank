library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Distribution"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("instrument", label = h4("Instrument"), 
                  choices = list("Words and Gestures" = "WG", "Words and Sentences" = "WS"), 
                  selected = 1),
      selectInput("measure", label = h4("Measure"), 
                  choices = list("Understands" = "understands", "Produces" = "produces"), 
                  selected = 1),
      selectInput("lang", label = h4("Language"), 
                  choices = list("English" = 1), 
                  selected = 1),
      selectInput("qsize", label = h4("Quantile size"), 
                  choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                  selected = 1),
      sliderInput("age", label = h4("Age (Months)"), 
                  min = 8, max = 36, value = 12)
      ),

    # Show a plot of the generated distribution
      mainPanel(
        plotOutput("plot")
      )
    )
  ))