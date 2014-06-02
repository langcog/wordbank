library(shiny)
#library(shinyIncubator)

shinyServer(function(input, output) {
  
  wordcloud_rep <-  repeatable(wordcloud)
  output$plot <- renderPlot({
    with(subset(wordle.data, wordle.data$age==input$age),
         wordcloud_rep(word,floor(vocab*100),
                       scale=c(2,.02),
                       min.freq = input$freq, 
                       max.words=input$max,
                       colors=brewer.pal(8, "Dark2")))
  })
  
})
