library(shiny)
library(wordcloud)
library(RMySQL)
library(dplyr)
library(ggplot2)
library(tidyr)
library(stringr)
source("../app_themes.R")

wscodes <- read.csv("../WS_codes.csv", stringsAsFactors=FALSE) 
wgcodes <- read.csv("../WG_codes.csv", stringsAsFactors=FALSE) 

## OPEN DATABASE CONNECTION ##
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")
wg.table <- tbl(wordbank,"instruments_wg")

## MERGE TABLES
ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_connthen)) %>%
  rename(id = basetable_ptr_id)

wg.vocab.words <- as.data.frame(select(wg.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_some)) %>%
  rename(id = basetable_ptr_id)

### GET DATA FROM INSTRUMENTS AND JOIN UP
ws.kid.words <- ws.vocab.words %>%
  gather(word,produces,col_baabaa:col_connthen)

wg.kid.words <- wg.vocab.words %>%
  gather(word,produces,col_baabaa:col_some) %>%
  mutate(produces = (produces ==2))

## MERGE IN KID DATA
admins <- as.data.frame(select(admin.table,data_id,child_id,age)) %>%
  rename(id = data_id, child.id = child_id)

children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order)) %>%
  rename(child.id = id)

child.data <- left_join(children,admins)

wordle.ws.data <- left_join(ws.kid.words, child.data) %>%
  mutate(word = str_replace(word, "col_", "")) %>%
  filter(age >= 16 & age <= 30) %>% 
  group_by(age,word) %>%
  summarise(vocab = mean(produces))

wordle.wg.data <- left_join(wg.kid.words, child.data) %>%
  mutate(word = str_replace(word, "col_", "")) %>%
  filter(age >= 8 & age <= 18) %>% 
  group_by(age,word) %>%
  summarise(vocab = mean(produces))

wordle.ws.data$word <- sapply(wordle.ws.data$word, 
                              function(w) wscodes[which(wscodes$code == w),
                                               "name"],
                           USE.NAMES = FALSE)

wordle.wg.data$word <- sapply(wordle.wg.data$word, 
                              function(w) wgcodes[which(wgcodes$code == w),
                                                  "name"],
                              USE.NAMES = FALSE)

shinyServer(function(input, output) {
  
  wordcloud_rep <- repeatable(wordcloud)
  
  ### FIELD SELECTOR
  output$age_selector_control <- renderUI({
    
    min.val = 8
    max.val = 16
    value = 13
    
    if(input$instrument == "WS") {
      min.val = 18
      max.val = 30
      value = 20
    }
    sliderInput("age", h4("Age (Months)"), min=min.val, 
                max = max.val, value = value)
  })
  
  output$plot <- renderPlot({
    
    if(is.null(input$instrument))
      return()
    
    data = wordle.wg.data
    scale = c(2,.05)
    
    if(input$instrument == "WS"){
      data = wordle.ws.data
      scale = c(1.5,.02)
    }

    with(filter(data, age==input$age),
         wordcloud_rep(word,floor(vocab*100),
                       scale=scale,
                       min.freq = input$freq, 
                       max.words=input$max,
                       colors=brewer.pal(8, "Dark2")))
  })
  
})
