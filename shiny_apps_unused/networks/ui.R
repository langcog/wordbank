library(shiny)
#library(shinyIncubator)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Semantic Network Statistics"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("n.measure", label = h4("Network Measure"), 
                  choices = list("Transitivity" = "coeff", 
                                 "Diameter" = "diam"), 
                  selected = 1),
      selectInput("demo.var", label = h4("Demographic Variable"), 
                  choices = list("Gender" = "gender", 
                                 "Mother's Education" = "mom_ed",
                                 "Birth Order" = "birth_order"), 
                  selected = 1)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("plot")
    )
  )
  ))