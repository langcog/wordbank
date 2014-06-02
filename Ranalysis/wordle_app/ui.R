library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Word Cloud"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("age", 
                  "Age (months):", 
                  min = 16,  max = 30, value = 16),
      sliderInput("freq", 
                  "Minimum Frequency:", 
                  min = 1,  max = 100, value = 50),
      sliderInput("max", 
                  "Maximum Number of Words:", 
                  min = 1,  max = 100,  value = 20)),
    
      # Show a plot of the generated distribution
      mainPanel(
        plotOutput("plot")
      )
    )
  ))