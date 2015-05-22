server <- function(input, output) {}
ui <- shinyUI(includeHTML("https://rawgit.com/langcog/wordbank/master/Ranalysis/sex_differences/sex_differences.html"))
shinyApp(ui = ui, server = server)