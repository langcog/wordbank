library(shiny)
library(wordcloud)
library(RMySQL)
library(dplyr)
library(ggplot2)
library(tidyr)
library(stringr)
source("../app_themes.R")

wscodes <- read.csv("../WS_codes.csv", stringsAsFactors=FALSE) 

## OPEN DATABASE CONNECTION ##
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")

## MERGE TABLES
ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_connthen)) %>%
  rename(id = basetable_ptr_id)

### GET DATA FROM INSTRUMENTS AND JOIN UP
ws.kid.words <- ws.vocab.words %>%
  gather(word,produces,col_baabaa:col_connthen)

## MERGE IN KID DATA
admins <- as.data.frame(select(admin.table,data_id,child_id,age)) %>%
  rename(id = data_id, child.id = child_id)

children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order)) %>%
  rename(child.id = id)

child.data <- left_join(children,admins)

wordle.data <- left_join(ws.kid.words, child.data) %>%
  mutate(word = str_replace(word, "col_", "")) %>%
  filter(age >= 16 & age <= 30) %>% 
  group_by(age,word) %>%
  summarise(vocab = mean(produces))

wordle.data$word <- sapply(wordle.data$word, 
                           function(w) wscodes[which(wscodes$code == w),"name"],
                           USE.NAMES = FALSE)

shinyServer(function(input, output) {
  wordcloud_rep <- repeatable(wordcloud)
  output$plot <- renderPlot({
    with(subset(wordle.data, wordle.data$age==input$age),
         wordcloud_rep(word,floor(vocab*100),
                       scale=c(1.5,.02),
                       min.freq = input$freq, 
                       max.words=input$max,
                       colors=brewer.pal(8, "Dark2")))
  })
  
})
