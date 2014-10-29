############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(ggvis)
library(dplyr)
library(reshape2)
library(RMySQL)
library(quantreg)
library(RSQLite)

## OPEN DATABASE CONNECTION ##
wordbank <- src_sqlite("~/Projects/Wordbank/wordbank/Ranalysis/wordbank.sqlite")
# wordbank <- src_mysql(dbname='wordbank',host="54.200.250.120", 
#                      user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")
wg.table <- tbl(wordbank,"instruments_wg")

## MERGE TABLES
wg.vocab.words <- as.data.frame(select(wg.table,
                                       basetable_ptr_id,col_baabaa:col_some))
ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,col_baabaa:col_connthen))
names(wg.vocab.words)[1] <- "id" # rename basetable_ptr_id
names(ws.vocab.words)[1] <- "id"

### GET DATA FROM INSTRUMENTS AND JOIN UP
wg.kid.words <- melt(wg.vocab.words,
                     id.vars="id",
                     variable.name = "word",
                     value.name = "score")
wg.kid.words <- wg.kid.words %>% 
  mutate(understands = score >= 1,
         produces = score == 2) %>%
  group_by(id) %>%
  summarise(understands = sum(understands),
            produces = sum(produces),
            instrument = "WG")

ws.kid.words <- melt(ws.vocab.words,
                     id.vars="id",
                     variable.name = "word",
                     value.name = "score")
ws.kid.words <- ws.kid.words %>% 
  mutate(understands = NA,
         produces = score == 1) %>%
  group_by(id) %>%
  summarise(understands = sum(understands),
            produces = sum(produces),
            instrument = "WS")

kid.words <- rbind(wg.kid.words, ws.kid.words)

## MERGE IN KID DATA
admins <- as.data.frame(select(admin.table,data_id,child_id,age))
children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order))
names(children)[1] <- "child.id"
names(admins)[1:2] <- c("id","child.id")

child.data <- left_join(children,admins)
kid.words <- left_join(kid.words, child.data)

qs <- .1 #as.numeric(input$qsize)
cuts <- seq(0.0,1.0, by=qs)
kid.words$vocab <- kid.words$produces
# kid.words <- eval(substitute(mutate(kid.words, vocab = var),
#                             list(var = as.name(input$measure))))

ddd <- kid.words %>% 
  filter(!is.na(vocab), instrument == "WG") %>% 
  group_by(age, instrument) %>%
  mutate(p = rank(vocab)/length(vocab),
         q = cut(p, breaks=cuts, 
                 labels=cuts[2:length(cuts)]-qs/2))

############ STUFF THAT RUNS WHEN USER LOADS PAGE ##############
# to run:
# runApp("~/Projects/Wordbank/wordbank/Ranalysis/norms_app")
# input <- list(instrument = "WS", measure = "produces", qsize = ".1")


shinyServer(function(input, output) {
  
  ############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
  
  values <- reactiveValues(selected = rep(TRUE, nrow(ddd)))
  
  ddd %>%
    ggvis(~age, ~vocab, fill = ~q) %>%
    layer_points() %>%
    group_by(q) %>%
    layer_model_predictions(model="loess", stroke = ~q) %>%
    add_axis("x", title="Age (months)") %>%
    add_axis("y", title="Vocabulary") %>%
    add_legend("fill", title = "Quantile Midpoint") %>%
    add_legend("stroke", title = "Quantile Midpoint") %>%
    handle_hover(function(data, ...) {
      values$selected <- ddd$vocab >= data$xmin_ &
        ddd$vocab < data$xmax_
    }) %>%
    bind_shiny("plot")
})

# selectInput("instrument", label = h3("Instrument"), 
#             choices = list("Words and Gestures" = "WG", "Words and Sentences" = "WS"), 
#             selected = 1),
# selectInput("measure", label = h3("Measure"), 
#             choices = list("Understands" = "understands", "Produces" = "produces"), 
#             selected = 1),
# selectInput("lang", label = h3("Language"), 
#             choices = list("English" = 1), 
#             selected = 1),
# selectInput("qsize", label = h3("Quantile size"), 
#             choices = list("10%" = .1, 
#                            "20%" = .2, "25%" = .25, 
#                            "33%" = .33),
#             selected = 1)),
