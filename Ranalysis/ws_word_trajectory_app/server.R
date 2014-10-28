############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(shiny)
library(ggplot2)
library(dplyr)
library(reshape2)
# library(RSQLite)
library(RMySQL)
library(quantreg)
library(directlabels)
theme_set(theme_bw())

## OPEN DATABASE CONNECTION ##
# wordbank <- src_sqlite("~/Projects/Wordbank/wordbank/Ranalysis/wordbank.sqlite")
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                     user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")

## MERGE TABLES
ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,col_baabaa:col_connthen))
names(ws.vocab.words)[1] <- "id"

### GET DATA FROM INSTRUMENTS AND JOIN UP
ws.kid.words <- melt(ws.vocab.words,
                     id.vars="id",
                     variable.name = "word",
                     value.name = "score")
ws.kid.words <- ws.kid.words %>% 
  mutate(produces = score == 1) 

## MERGE IN KID DATA
admins <- as.data.frame(select(admin.table,data_id,child_id,age))
children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order))
names(children)[1] <- "child.id"
names(admins)[1:2] <- c("id","child.id")

child.data <- left_join(children,admins)
kid.words <- left_join(ws.kid.words, child.data)      

kid.words$word <- str_replace(kid.words$word, "col_","")

############ STUFF THAT RUNS WHEN USER LOADS PAGE ##############
# to run:
# runApp("~/Projects/Wordbank/wordbank/Ranalysis/norms_app")
# input <- list(word1 = "baabaa", word2 = "break", word3 = "cat")

shinyServer(function(input, output) {
  
  ############## STUFF THAT RUNS WHEN USER CHANGES SOMETHING ##############
  output$plot <- renderPlot({
    
        
    ddd <- kid.words %>% 
      filter(word == input$word1 |
               word == input$word2 |
               word == input$word3) %>% 
      filter(age > 16 & age < 36) %>%
      group_by(age,word) %>%
      summarise(p = mean(score))
    
    qplot(age, p, col=word, data=ddd) + 
      geom_smooth(se=FALSE) + 
      xlab("Age (months)") + 
      ylab("Proportion of Children Producing") + 
      scale_colour_discrete(guide=FALSE) + 
      xlim(c(16,37)) + 
      ylim(c(0,1)) + 
      geom_dl(aes(label=word), method = list(dl.trans(x=x +.2),"last.qp",cex=1))
  })
})
