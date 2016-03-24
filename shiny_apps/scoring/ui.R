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
               "To use it, upload a tab- or comma-delimited file.",
               "The file must contain columns for vocabulary size (number of words checked on the form), age (months), and gender, and can optionally contain other columns.",
               "These fields are then used to look up gender-specific percentiles.",
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