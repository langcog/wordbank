library(shiny)
library(shinythemes)
library(shinyBS)

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Item Trajectories"),
                             "This analysis allows exploration of growth curves for individual words on a CDI form. The experimental \"both\" option shows data from multiple forms for the same language.",
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
        bsPopover("language_selector", title = NULL, 
                  content = HTML("See contributors page for citation info."), 
                  placement = "right"),
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL, 
                  content = HTML("Words & Gestures for infants and toddlers, Words & Sentences for toddlers and young preschoolers, Both to integrate across the two."), 
                  placement = "right"),
        uiOutput("measure_selector"),
        bsPopover("measure_selector", title = NULL, 
                  content = HTML("Question that parents were asked to answer."), 
                  placement = "right"),
        selectInput("words", label = h4("Words"),
                    choices = NULL, multiple = TRUE),
#         selectInput("wordform", label = h4("Wordforms"),
#                     choices = NULL, multiple = TRUE),
#         selectInput("complexity", label = h4("Complexity"),
#                     choices = NULL, multiple = TRUE),
#         bsPopover("words", title = NULL, 
#                   content = HTML("Choose words to be plotted by typing or selecting from the list."), 
#                   placement = "right"),
        br(),
        downloadButton('downloadPlot', 'Download Plot', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadTable', 'Download Table', class = "btn-primary btn-sm"),
#         br(),br(),
#         downloadButton('downloadData', 'Download Raw Data', class = "btn-primary btn-sm"),
        width=3)),
    
    # Show a plot of the generated distribution
    mainPanel(
      width=9,      
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      tabsetPanel(
        tabPanel("Plot",
                 br(),
                  conditionalPanel(
                    condition = "output.loaded == 1",
                    plotOutput("plot", width = "100%", height = "auto"),
                    br(),
                    bsCollapse(id = "details", open = NULL,
                               bsCollapsePanel("More details...",
                                               includeMarkdown("details.md"),
                                               style = "default"))
                  )
        ),
        tabPanel("Table",
                 br(),
                 tableOutput("table"))
      )
    )
  )
))