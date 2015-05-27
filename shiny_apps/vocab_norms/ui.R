library(shiny)
library(shinythemes)
library(shinyBS)


shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
#  titlePanel("Vocabulary Norms"),
#  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = titlePanel("Vocabulary Norms"),
                             "This report shows growth curves for vocabulary size for different languages and measures (whether a child produces or understands a particular number of words). For some datasets, it is possible to compare growth curves across different demographic groups (e.g., sex, mother's education).",
                             value = "title",
                             style = "default")),

  sidebarLayout(
    sidebarPanel(
      width=3,
      
      conditionalPanel(
        condition = "output.loaded != 1",
        h4("Loading...")
      ),
      
      conditionalPanel(
        condition = "output.loaded == 1",
        uiOutput("language_selector"),
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL, content = "Words & Gestures is for infants and toddlers, Words & Sentences is for toddlers and young preschoolers", placement = "right"),
        uiOutput("measure_selector"),
        uiOutput("demo_selector"),
        bsPopover("demo_selector", title = NULL, content = "Demographic variables split or group the dataset", placement = "right"),
        selectInput("quantiles", label = h4("Quantiles"),
                    choices = list("Standard", "Deciles", "Quintiles", "Quartiles", "Median"),
                    selected = "Standard"),
        bsPopover("quantiles", title = NULL, content = "Cut points for percentile curves", placement = "right"),
        br(),
        downloadButton('downloadPlot', 'Download Plot'),
        br(),br(),
        downloadButton('downloadData', 'Download Data')
      )),
    
    mainPanel(
      width=9,
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
      conditionalPanel(
        condition = "output.loaded == 1",
        plotOutput("plot", width = "100%", height = "auto"),
        h5("Sample sizes:"),
        tableOutput("sample_sizes"),
        bsCollapse(id = "details", open = NULL,
                   bsCollapsePanel("More details",
                                   htmlOutput("details"),
                                   style = "info"))
      )
    )
  )
))