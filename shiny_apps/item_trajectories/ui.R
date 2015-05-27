library(shiny)
library(shinythemes)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Item Trajectories"),
                             "This analysis allows exploration of growth curves for individual words (as well as word categories and other questions on particular forms).",
                             value = "title",
                             style = "default")),
    
  sidebarLayout(
    sidebarPanel(
      width=3,
      
      conditionalPanel(
        condition="output.loaded != 1",
        h4("Loading...")
      ),
      
      conditionalPanel(
        condition="output.loaded == 1",
        
        uiOutput("language_selector"),
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL, content = "Words & Gestures is for infants and toddlers, Words & Sentences is for toddlers and young preschoolers", placement = "right"),
        uiOutput("measure_selector"),
        selectInput("words", label = h4("Words"),
                    choices = NULL, multiple = TRUE),
#         selectInput("wordform", label = h4("Wordforms"),
#                     choices = NULL, multiple = TRUE),
#         selectInput("complexity", label = h4("Complexity"),
#                     choices = NULL, multiple = TRUE),
        br(),
        downloadButton('downloadPlot', 'Download Plot', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadData', 'Download Data', class = "btn-primary btn-sm"),
        width=3)),
    
    # Show a plot of the generated distribution
    mainPanel(
      width=9,      
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"
      ),
      conditionalPanel(
        condition = "output.loaded == 1",
        plotOutput("plot", width = "100%", height = "auto"),
        br(),
        bsCollapse(id = "details", open = NULL,
                   bsCollapsePanel("More details",
                                   includeMarkdown("details.md"),
                                   style = "info"))
      )
    )
  )
))