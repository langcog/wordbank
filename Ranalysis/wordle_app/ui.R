library(shiny)
#library(shinyIncubator)
 
shinyUI(fluidPage(
 
  # Application title
  titlePanel("Word Cloud"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("age", 
                  "Age (months):", 
                  min = 16,  max = 30, value = 16)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("plot")
    )
  )
))