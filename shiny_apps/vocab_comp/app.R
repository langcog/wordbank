server <- function(input, output) {}
ui <- shinyUI(includeHTML("https://rawgit.com/mikabr/vocab-comp/master/vocab_comp.html"))
shinyApp(ui = ui, server = server)