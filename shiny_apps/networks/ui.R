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
        selectInput("instrument", "CDI Instrument for measuring age of acquisition",
                       choices = c("Words & Sentences" = "WS", 
                                   "Words & Gestures" = "WG"),
                       selected = "production"),
        uiOutput("measure"),
        selectInput("assocs", "Association type",
                       choices = c("Conceptual" = "conceptual", 
                                   "Perceptual" = "perceptual", 
                                   "All" = "all"),
                       selected = "all"),
        sliderInput("age", "Age of Acquisition",
                    min = 6, 
                    max = 36, 
                    value = 20, step = 1),
        sliderInput("cutoff", "Minimum semantic associations",
                    min = 1, max = max(assoc_edges$width), 
                    value = 2, step = 1),
        selectizeInput("weighted", "Should graph edges be weighted?",
                    choices = c("Yes" = TRUE, 
                                "No" = FALSE),
                    selected = TRUE),
        selectizeInput("group", "Grouping variable",
                       choices = c("None" = "identity", 
                                   "CDI category" = "category"),
                       selected = "identity"),
        width = 3)),
    
    mainPanel(
      width = 9,
      tags$style(type = "text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      conditionalPanel(
        condition = "output.loaded == 1",
        visNetworkOutput("network", height = "500px")
      )
    )
  )
))
