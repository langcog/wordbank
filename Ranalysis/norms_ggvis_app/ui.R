library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Vocabulary Norms"),
  
  sidebarLayout(
    sidebarPanel(
      uiOutput("ggvis_ui")
      ),
      

    # Show a plot of the generated distribution
      mainPanel(        
        ggvisOutput("plot")
      )
    )
  ))

# ,