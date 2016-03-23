library(shiny)
library(shinythemes)
library(shinyBS)


shinyUI(fluidPage(
  theme = shinytheme("spacelab"),
  
  br(),
  bsCollapse(id = "doc", open = "title",
             bsCollapsePanel(
               title = h3("CDI Administration Scoring"),
               "This app is a scoring tool for MB-CDI administrations, using the Fenson et al. (2007) revised norming data.",
               # "To use it, upload a tab- or comma-separated file with a column indicating the number of words the child knows.",
               value = "title",
               style = "default")),

  sidebarLayout(
    sidebarPanel(
      h4("1. Download a sample template"),
      downloadButton('downloadSample', 'Download'),
      tags$hr(),
      h4("2. Upload your own data"), 
      fileInput('file1', 'Choose file',
                accept=c('text/csv', 
                         'text/comma-separated-values,text/plain', 
                         '.csv')),
      tags$hr(),
      h4("3. Select the instrument to use"), 
      selectInput('instrument', label=NULL, 
                  choices = c("Words & Sentences (English)" = "Words & Sentences (English)")),
      tags$hr(),
      h4("4. Verify file formatting"), 
      # checkboxInput('header', 'Header', TRUE),
      radioButtons('sep', label=NULL, inline=TRUE,
                   c("Comma delimited" = ',',
                     "Tab delimited"='\t'),
                   ','),
      radioButtons('quote', label=NULL, inline=TRUE,
                   c("No quotes"='',
                     'Double quotes'='"',
                     'Single quotes'="'"),
                   ''), 
      uiOutput('ageColumn'),
      uiOutput('nwordsColumn'),
      uiOutput('genderColumn'),
      uiOutput('genderMappings')
    ),
    mainPanel(
      uiOutput('tableTitle'),
      uiOutput('download'), 
      br(),
      dataTableOutput('contents')
    )
  )
))