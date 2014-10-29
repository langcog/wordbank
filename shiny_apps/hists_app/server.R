############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(ggplot2)
library(dplyr)
library(reshape2)
# library(RSQLite)
library(RMySQL)
library(quantreg)
source("../app_themes.R")

## OPEN DATABASE CONNECTION ##
# wordbank <- src_sqlite("~/Projects/Wordbank/wordbank/Ranalysis/wordbank.sqlite")
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                     user="wordbank",password="wordbank")

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

lims <- data.frame(instrument = c("WG","WS"),
                   lim = c(396,680))

############ STUFF THAT RUNS WHEN USER LOADS PAGE ##############
# to run:
# runApp("~/Projects/Wordbank/wordbank/Ranalysis/norms_app")
# input <- list(instrument = "WG", measure = "understands", qsize = ".1", age=18)

shinyServer(function(input, output) {
  
  ############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
  output$plot <- renderPlot({
    
    qs <- as.numeric(input$qsize)
    cuts <- seq(0.0,1.0, by=qs)
    kid.words <- eval(substitute(mutate(kid.words, vocab = var),
                                 list(var = as.name(input$measure))))
        
    ddd <- kid.words %>% 
      filter(!is.na(vocab), 
             instrument == input$instrument) %>% 
      filter(age == input$age) %>%
      group_by(age) %>%
      mutate(p = rank(vocab)/length(vocab),
             q = cut(p, breaks=cuts, 
                     labels=cuts[2:length(cuts)]-qs/2))
    
    qplot(vocab, data=ddd, fill=q, binwidth=25) + 
      xlab("Vocabulary") + ylab("Number of Children") + 
      scale_fill_discrete(name="Quantile Midpoint") + 
      xlim(c(0,lims$lim[lims$instrument == input$instrument])) + 
      ylim(c(0,100))
  })
})
