library(shiny)
library(shinythemes)
library(shinyBS)
library(markdown)
library(visNetwork)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Semantic Networks"),
                             includeMarkdown("docs/description.md"),
                             value = "title",
                             style = "default")),
  
  sidebarLayout(
    sidebarPanel(
      width = 3,
      conditionalPanel(
        condition = "output.loaded != 1",
        h4("Loading...")
      ),
      
      conditionalPanel(
        condition = "output.loaded == 1",
        selectInput("source", "Network Source",
                    choices = c("McRae Feature Norms" = "MFN", 
                                "Word2Vec Model" = "W2V"), 
                                # "Picture Book Model" = "PB"),
                    selected = "W2V"),
        selectInput("instrument", "CDI Instrument",
                       choices = c("Words & Sentences" = "WS", 
                                   "Words & Gestures" = "WG"),
                       selected = "production"),
        uiOutput("measure"),
        uiOutput("assoc_control"),
        sliderInput("age", "Age of Acquisition",
                    min = 6, 
                    max = 36, 
                    value = 20, step = 1),
        uiOutput('cutoff'),
        selectizeInput("weighted", "Should graph edges be weighted?",
                    choices = c("Yes" = TRUE, 
                                "No" = FALSE),
                    selected = TRUE),
        selectizeInput("group", "Grouping variable",
                       choices = c("None" = "identity", 
                                   "CDI category" = "category",
                                   "Lexical category" = "lexical_category"),
                       selected = "identity"),
        width = 3)),
    
    mainPanel(
      width = 9,
      tags$style(type = "text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      conditionalPanel(
        condition = "output.loaded == 1",
        visNetworkOutput("network", height = "800px")
      )
    )
  )
))
