server <- function(input, output) {}
ui <- shinyUI(includeHTML("https://rawgit.com/dyurovsky/cdi-grammar/master/grammar_lex.html"))
shinyApp(ui = ui, server = server)