library(shiny)
library(shinythemes)
library(shinyBS)


shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
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
        uiOutput("language_selector"),
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL, content = "Words & Gestures is for infants and toddlers, Words & Sentences is for toddlers and young preschoolers", placement = "right"),
        uiOutput("measure_selector"),
        uiOutput("demo_selector"),
        bsPopover("demo_selector", title = NULL, content = "Demographic variable to split or group the dataset", placement = "right"),
        selectInput("quantiles", label = h4("Quantiles"),
                    choices = list("Standard", "Deciles", "Quintiles", "Quartiles", "Median"),
                    selected = "Standard"),
        bsPopover("quantiles", title = NULL, content = "Cut points for percentile curves", placement = "right"),
        br(),
        downloadButton('downloadPlot', 'Download Plot', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadData', 'Download Data', class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton('downloadCurves', 'Download Curves', class = "btn-primary btn-sm")
      )),
    
    mainPanel(
      width=9,
      tags$style(type="text/css",
                 ".shiny-output-error { visibility: hidden; }",
                 ".shiny-output-error:before { visibility: hidden; }"),
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