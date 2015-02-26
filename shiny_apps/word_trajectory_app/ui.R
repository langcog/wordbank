library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Word Production/Comprehension Trajectory"),
  
  sidebarLayout(
    sidebarPanel(
#      selectInput("language", label = h4("Language"), 
#                  choices = list("English" = "English"), 
#                  selected = 1),
#      selectInput("form", label = h4("Form"), 
#                  choices = list("Words and Sentences" = "WS",
#                                 "Words and Gestures" = "WG"), 
#                  selected = 1),
      uiOutput("language_selector_control"),
      uiOutput("form_selector_control"),      
      uiOutput("measure_selector_control"),
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