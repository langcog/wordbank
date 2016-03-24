library(shiny)
library(shinythemes)
library(shinyBS)
library(jsonlite)

pops <- fromJSON("docs/popovers.json")

shinyUI(fluidPage(

  theme = shinytheme("spacelab"),

  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Vocabulary Norms"),
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
        tags$style(type = "text/css", ".popover { width: 150px; }"),
        uiOutput("language_selector"),
        bsPopover("language_selector", title = NULL,
                  content = HTML(sprintf("<small>%s</small>", pops$language)),
                  placement = "right"),
        uiOutput("form_selector"),
        bsPopover("form_selector", title = NULL,
                  content = HTML(sprintf("<small>%s</small>", pops$form)),
                  placement = "right"),
        uiOutput("measure_selector"),
        bsPopover("measure_selector", title = NULL,
                  content = HTML(sprintf("<small>%s</small>", pops$measure)),
                  placement = "right")),

      conditionalPanel(
        condition = "output.loaded == 1",
        uiOutput("data_filter"),
        uiOutput("demo_selector"),
        bsPopover("demo_selector", title = NULL,
                  content = HTML(sprintf("<small>%s</small>", pops$demo)),
                  placement = "right"),
        selectInput("quantiles", label = h4("Quantiles"),
                    choices = list("Standard", "Deciles", "Quintiles",
                                   "Quartiles", "Median"),
                    selected = "Standard"),
        bsPopover("quantiles", title = NULL,
                  content = HTML(sprintf("<small>%s</small>", pops$quantile)),
                  placement = "right"),
        br(),
        downloadButton("download_plot", "Download Plot",
                       class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton("download_table", "Download Table",
                       class = "btn-primary btn-sm"),
        br(),br(),
        downloadButton("download_data", "Download Raw Data",
                       class = "btn-primary btn-sm")
      )),

    mainPanel(
      width = 9,
      tags$style(type = "text/css",
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
                              bsCollapsePanel(
                                "More details...",
                                includeMarkdown("docs/details.md"),
                                style = "primary")
                   )
                 )),
        tabPanel("Table",
                 br(),
                 tableOutput("table"))
      )
    )
  )
))
