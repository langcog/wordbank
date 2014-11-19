library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Word Production/Comprehension Trajectory"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("lang", label = h4("Language"), 
                  choices = list("English" = 1), 
                  selected = 1),
      selectInput("instrument", label = h4("Instrument"), 
                  choices = list("Words and Sentences" = "WS",
                                 "Words and Gestures" = "WG"), 
                  selected = 1),
      uiOutput("field_selector_control"),
      uiOutput("word1_selector"),
      uiOutput("word2_selector"),
      uiOutput("word3_selector")),

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