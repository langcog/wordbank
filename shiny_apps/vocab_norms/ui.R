library(shiny)
library(shinythemes)
library(shinyBS)


shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Vocabulary Norms"),
                             "This analysis shows growth curves for vocabulary size, the number of words that a child produces or understands, for different languages, forms, and measures.",
                             "For some datasets, it is possible to compare growth curves across different demographic groups (birth order, ethnicity, sex, mother's education).",
                             "Use a median quantile type to compare demographic groups on a single plot, or other quantile sizes to see separate curves and plots for each groups.",
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
        tags$style(type = "text/css", ".popover { width: 150px; }"),
        uiOutput("language_selector"),
        bsPopover("language_selector", title = NULL, 
                  content = HTML("<small>see contributors page for citation info</small>"),
                  placement = "right"),        
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL,
                  content = HTML("<small>Words & Gestures for infants and toddlers, Words & Sentences for toddlers and young preschoolers</small>"),
                  placement = "right"),
        uiOutput("measure_selector"),
        bsPopover("measure_selector", title = NULL, 
                  content = HTML("<small>question that parents were asked to answer</small>"),
                  placement = "right"),
        uiOutput("demo_selector"),
        bsPopover("demo_selector", title = NULL,
                  content = HTML("<small>demographic variable to split or group the dataset</small>"),
                  placement = "right"),
        selectInput("quantiles", label = h4("Quantiles"),
                    choices = list("Standard", "Deciles", "Quintiles", "Quartiles", "Median"),
                    selected = "Standard"),
        bsPopover("quantiles", title = NULL,
                  content = "<small>cut points for percentile curves</small>",
                  placement = "right"),
        br(),
        downloadButton('downloadPlot', 'Download Plot', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadTable', 'Download Table', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadData', 'Download Raw Data', class = "btn-primary btn-sm")
      )),
    
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
                 )),
        tabPanel("Table",
                 br(),
                 tableOutput("table"))
      )
    )
  )
))