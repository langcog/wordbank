#, wordform = NULL, complexity = NULL)

#   if(!is.null(input_wordform)) {
#     wordform.data <- get.instrument.data(instrument.table, input_wordform) %>%
#       mutate(produces = value == 'produces') %>%
#       select(-value) %>%
#       left_join(admins) %>%
#       group_by(item_id, age) %>%
#       summarise(score = mean(produces, na.rm=TRUE)) %>%
#       rowwise %>%
#       mutate(item = instrument$wordform.by.id[[1]][[paste("item_", item_id, sep="")]],
#              type = 'wordform')
#   } else {wordform.data <- data.frame()}
#
#   if(!is.null(input_complexity)) {
#     complexity.data <- get.instrument.data(instrument.table, input_complexity) %>%
#       mutate(complex = value == 'complex') %>%
#       select(-value) %>%
#       left_join(admins) %>%
#       group_by(item_id, age, form) %>%
#       summarise(score = mean(complex, na.rm=TRUE)) %>%
#       rowwise %>%
#       mutate(item = instrument$complexity.by.id[[1]][[paste("item_", item_id, sep="")]],
#              type = 'complexity')
#   } else {complexity.data <- data.frame()}

#  bind_rows(word.data, wordform.data, complexity.data)
#}

#     wordform.by.definition = list_items_by_definition(filter(items,
#                                                             instrument_id==.$instrument_id,
#                                                             type=='word_form')),
#     wordform.by.id = list_items_by_id(filter(items,
#                                             instrument_id==.$instrument_id,
#                                             type=='word_form')),
#     complexity.by.definition = list_items_by_definition(filter(items,
#                                                               instrument_id==.$instrument_id,
#                                                               type=='complexity')),
#     complexity.by.id = list_items_by_id(filter(items,
#                                               instrument_id==.$instrument_id,
#                                               type=='complexity'))) %>%

# input_wordform <- reactive(input$wordform)
# input_complexity <- reactive(input$complexity)

#  observe({
#     wordforms <- filter(instrument_tables,
#                         language == input_language(),
#                         form == input_form())$wordform.by.definition[[1]]
#     updateSelectInput(session, 'wordform', choices = wordforms, selected = "")
#  })

#  observe({
#     complexity <- filter(instrument_tables,
#                          language == input_language(),
#                          form == input_form())$complexity.by.definition[[1]]
#     updateSelectInput(session, 'complexity', choices = complexity, selected = "")
#  })


#         selectInput("wordform", label = h4("Wordforms"),
#                     choices = NULL, multiple = TRUE),
#         selectInput("complexity", label = h4("Complexity"),
#                     choices = NULL, multiple = TRUE),
