library(shiny)
library(shinythemes)
library(shinyBS)
library(jsonlite)


pops <- fromJSON("docs/popovers.json")

shinyUI(fluidPage(
  
  theme = shinytheme("spacelab"),
  
  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(title = h3("Item Trajectories"),
                             includeMarkdown("docs/description.md"),
                             value = "title",
                             style = "default")),
  
  fluidRow(
    column(3,
           conditionalPanel(
             condition = "output.loaded != 1",
             h4("Loading...")
           ),
           
           conditionalPanel(
             condition = "output.loaded == 1",
             
             wellPanel(
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
                         placement = "right"),
               uiOutput("data_filter")),
             
             wellPanel(
               popify(selectInput("words", label = strong("Words"),
                                  choices = NULL, multiple = TRUE),
                      title = NULL,
                      content = HTML(sprintf("<small>%s</small>", pops$words)),
                      placement = "right"))
           )),
    
    column(9,
           tags$style(type = "text/css",
                      ".shiny-output-error { visibility: hidden; }",
                      ".shiny-output-error:before { visibility: hidden; }"),
           tabsetPanel(
             tabPanel("Plot",
                      br(),
                      conditionalPanel(
                        condition = "output.loaded == 1",
                        bsAlert("many_words"),
                        #br(),
                        plotOutput("trajectory_plot", width = "100%",
                                   height = "auto"),
                        br(),
                        downloadButton("download_plot", "Download Plot",
                                       class = "btn-default btn-xs"),
                        br(),br(),
                        bsCollapse(
                          id = "details", open = NULL,
                          bsCollapsePanel("More details...",
                                          includeMarkdown("docs/details.md"),
                                          style = "default"))
                      )
             ),
             tabPanel("Table",
                      br(),
                      downloadButton("download_table", "Download Table",
                                     class = "btn-default btn-xs"),
                      br(), br(),
                      tableOutput("table"))
           )
    )
  )
))
