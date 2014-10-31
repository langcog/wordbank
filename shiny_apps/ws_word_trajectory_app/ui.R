library(shiny)
library(stringr)
# wscodes <- read.csv("~/Projects/Wordbank/wordbank/Ranalysis/word_trajectory_app/WS_codes.csv")
wscodes <- read.csv("../WS_codes.csv")
wscodes <- wscodes[order(wscodes[,1]),]

words <- list()
words$"Select Word" <- ""
for (i in 1:length(wscodes$name)) {
  wdname <- str_replace_all(wscodes[i,2],"[^[:alnum:]]","")
  wdcode <- wscodes[i,1]
  eval(parse(text=paste("words$",wdname,"='",wdcode,"'",sep="")))
}


shinyUI(fluidPage(
  
  # Application title
  titlePanel("Word Production Trajectory (Words & Sentences)"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("lang", label = h4("Language"), 
                  choices = list("English" = 1), 
                  selected = 1),
      selectInput("word1", label = h4("Word 1"), 
                  choices = words,
                  selected = 1),
      selectInput("word2", label = h4("Word 2"), 
                  choices = words,
                  selected = 2),
      selectInput("word3", label = h4("Word 3"), 
                  choices = words,
                  selected = 3)
      ),

    # Show a plot of the generated distribution
      mainPanel(
        plotOutput("plot")
      )
    )
  ))