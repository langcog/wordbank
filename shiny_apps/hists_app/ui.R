library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Distribution"),
  
  sidebarLayout(
    sidebarPanel(
      uiOutput("language_selector"),
      uiOutput("form_selector"),      
      uiOutput("measure_selector"),
      
      selectInput("qsize", label = h4("Quantile size"), 
                  choices = list("10%" = .1, "20%" = .2, "25%" = .25),
                  selected = 1),
      sliderInput("age", label = h4("Age (Months)"), 
                  min = 8, max = 36, value = 24)
      ),

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