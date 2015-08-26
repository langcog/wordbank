library(shiny)
library(dplyr)
library(readr)

lookup <- read_csv("lookup.csv")

# input$file1 will be NULL initially. After the user selects
# and uploads a file, it will be a data frame with 'name',
# 'size', 'type', and 'datapath' columns. The 'datapath'
# column will contain the local filenames where the data can
# be found.

shinyServer(function(input, output) {
  data <- reactive({
    inFile <- input$file1
    
    if (is.null(inFile))
      return(NULL)
    
    d <- read.csv(inFile$datapath, header=input$header, sep=input$sep, 
                  quote=input$quote)
    
    left_join(d, lookup)
  })
  
  output$contents <- renderTable({
    data()
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { 
      paste0("percentiles.csv") 
    },
    content = function(file) {
      write_csv(data(), file)
    }
  )
})