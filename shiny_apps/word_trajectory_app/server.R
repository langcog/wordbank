############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(ggplot2)
library(dplyr)
library(RMySQL)
library(directlabels)
library(tidyr)
library(stringr)
source("../app_themes.R")

# READ IN ENGLISH LABELS FOR WORDS
wscodes <- read.csv("../WS_codes.csv")  %>%
  arrange(code)
wgcodes <- read.csv("../WG_codes.csv") %>%
  arrange(code)

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
  mutate(understands = (produces == 1),
    produces = (produces ==2))

## MERGE IN KID DATA
admins <- as.data.frame(select(admin.table,data_id,child_id,age)) %>%
  rename(id = data_id, child.id = child_id)

children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order)) %>%
  rename(child.id = id)

child.data <- left_join(children,admins)

ws.data <- left_join(ws.kid.words, child.data) %>%
  mutate(word = str_replace(word, "col_", "")) %>%
  filter(age >= 16 & age <= 30) %>% 
  group_by(age,word) %>%
  summarise(produces = mean(produces))

wg.data <- left_join(wg.kid.words, child.data) %>%
  mutate(word = str_replace(word, "col_", "")) %>%
  filter(age >= 8 & age <= 18) %>% 
  group_by(age,word) %>%
  summarise(produces = mean(produces),
            understands = mean(understands))

ws.data$word <- sapply(ws.data$word, 
                              function(w) wscodes[which(wscodes$code == w),
                                                  "name"],
                              USE.NAMES = FALSE)

wg.data$word <- sapply(wg.data$word, 
                              function(w) wgcodes[which(wgcodes$code == w),
                                                  "name"],
                              USE.NAMES = FALSE)

# WORD SELECTORS
ws.words <- list()
ws.words$"Select Word" <- ""
for (i in 1:length(wscodes$name)) {
  wdname <- paste("\"",wscodes[i,2],"\"",sep="")
  wdcode <- wscodes[i,2]
  eval(parse(text=paste("ws.words$",wdname,"=\"",wdcode,"\"",sep="")))
}

wg.words <- list()
wg.words$"Select Word" <- ""
for (i in 1:length(wgcodes$name)) {
  wdname <- paste("\"",wgcodes[i,2],"\"",sep="")
  wdcode <- wgcodes[i,2]
  eval(parse(text=paste("wg.words$",wdname,"=\"",wdcode,"\"",sep="")))
}

############ STUFF THAT RUNS WHEN USER LOADS PAGE ##############
# to run:
# runApp("~/Projects/Wordbank/wordbank/Ranalysis/norms_app")
# input <- list(word1 = "baabaa", word2 = "break", word3 = "cat")

shinyServer(function(input, output) {
  
  ############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
  output$plot <- renderPlot({
    
    if(is.null(input$instrument))
      return()
    
    data = ws.data %>%
      filter(word == input$word1 |
                     word == input$word2 |
                     word == input$word3) %>% 
      group_by(age,word) %>%
      summarise(p = mean(produces))
    
    xlims = c(16,32)
    xbreaks = 16:30
    
    if(input$instrument == "WG"){
      data = wg.data %>%
        filter(word == input$word1 |
                 word == input$word2 |
                 word == input$word3) %>% 
        group_by(age,word)
      
      if(input$measure=="understands"){
        data <- summarise(data,p=mean(understands))
      } else {
        data <- summarise(data,p=mean(produces))
      }
      
      xlims = c(8,20)
      xbreaks = 8:18
    }
       
    ggplot(data, aes(x=age, y=p,colour=word,label=word))+
      geom_smooth(se=FALSE,method="loess") +
      geom_point()+
      scale_x_continuous(breaks=xbreaks,
                         limits=xlims,
                         name = "Age (months)")+
      scale_y_continuous(name = "Proportion of Children Producing",
                         limits=c(-.01,1),
                         breaks=seq(0,1,.25)) +
      theme_bw(base_size=14) + 
      theme(legend.position="none") +
      geom_dl(method = list(dl.trans(x=x +.2),"last.qp",cex=1))+
      scale_colour_brewer(palette="Set1") 
  })
  
  ### FIELD SELECTOR
  output$field_selector_control <- renderUI({
    if (input$instrument == "WG") {
      fields <- list("Produces" = "produces","Understands" = "understands")
    } else if (input$instrument == "WS") {
      fields <- list("Produces" = "produces")
    }
    selectInput("measure", h4("Measure"), fields, selectize = TRUE)
  })
  
  ### WORD SELECTORS
  output$word1_selector <- renderUI({
    if (input$instrument == "WG") {
      words = wg.words
    } else if (input$instrument == "WS") {
      words = ws.words
    }
    selectInput("word1", h4("Word1"), choices=words, selectize = TRUE,
                selected = 1)
  })
    
  output$word2_selector <- renderUI({ 
    if (input$instrument == "WG") {
      words = wg.words
    } else if (input$instrument == "WS") {
      words = ws.words
    }
    selectInput("word2", h4("Word2"), choices=words, selectize = TRUE,
                selected = 1)
  })
  
  output$word3_selector <- renderUI({
    if (input$instrument == "WG") {
      words = wg.words
    } else if (input$instrument == "WS") {
      words = ws.words
    }
    selectInput("word3", h4("Word3"), choices=words, selectize = TRUE,
                selected = 1)
  })
})
