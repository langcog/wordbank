# clear all previous variables
rm(list=ls())

# set path to script folder
setwd('~/Documents/projects/wordbank/Ranalysis')
source('~/Documents/projects/Ranalysis/useful.R')

#load libraries for data manipulation and graphing
library(ggplot2)
library(directlabels)
library(dplyr)
library(tidyr)
library(reshape2)
library(RSQLite)
library(RSQLite.extfuns)
library(RMySQL)

# connect to local databse
#wordbank <- src_sqlite('wordbank.sqlite')
#wordbank <- src_mysql(dbname='wordbank')

wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

# load all tables
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
instruments.table <- tbl(wordbank,"common_instrumentsmap")
source.table <- tbl(wordbank,"common_source")
wordinfo.table <- tbl(wordbank,"common_wordinfo")
mapping.table <- tbl(wordbank,"common_wordmapping")
cdicat.table <- tbl(wordbank,"common_cdicategory")
ws.table <- tbl(wordbank,"instruments_ws")
wg.table <- tbl(wordbank,"instruments_wg")

wg.vocab.words <- as.data.frame(select(wg.table,
                                       basetable_ptr_id,col_baabaa:col_some))
ws.vocab.words <- as.data.frame(select(ws.table,
                                      basetable_ptr_id,col_baabaa:col_connthen))
names(wg.vocab.words)[1] <- "id"
names(ws.vocab.words)[1] <- "id"

# arrange vocab data by kid and word
wg.kid.words <- melt(wg.vocab.words,
                     id.vars="id",
                     variable.name = "word",
                     value.name = "score")
wg.kid.words = mutate(wg.kid.words, 
                      understands = score >= 1,
                      produces = score == 2)

ws.kid.words <- melt(ws.vocab.words,
                     id.vars="id",
                     variable.name = "word",
                     value.name = "score")
ws.kid.words = mutate(ws.kid.words, 
                     understands = score == 1,
                     produces = score == 1)

wg.kid.words <- mutate(wg.kid.words,
                       lemma = substr(word, 5, length(word)))
ws.kid.words <- mutate(ws.kid.words,
                       lemma = substr(word, 5, length(word)))

sources <- as.data.frame(source.table)
names(sources)[1] <- 'source_id'

admins <- as.data.frame(select(admin.table,data_id,child_id,age,source_id))
children <- as.data.frame(select(child.table,id,gender))
child.data <- merge(children,admins,by.y="child_id",by.x = "id")

child.source.data <- merge(child.data, sources)

word.info <- as.data.frame(wordinfo.table)
cdi.cat <- as.data.frame(cdicat.table)
names(cdi.cat)[1] <- "CDI_cat_id"
names(cdi.cat)[2] <- "category"

word.cats <- merge(word.info, cdi.cat)
wg.kid.word.data <- merge(wg.kid.words, word.cats)
ws.kid.word.data <- merge(ws.kid.words, word.cats)

wg.vocab.sizes <- wg.kid.word.data %>%
  group_by(id) %>%
  summarise(productive = sum(produces),
            receptive = sum(understands))
wg.cat.sizes <- wg.kid.word.data %>%
  group_by(id, category) %>%
  summarise(productive = sum(produces),
            receptive = sum(understands))

ws.vocab.sizes <- ws.kid.word.data %>%
  group_by(id) %>%
  summarise(productive = sum(produces),
            receptive = sum(understands))
ws.cat.sizes <- ws.kid.word.data %>%
  group_by(id, category) %>%
  summarise(productive = sum(produces),
            receptive = sum(understands))

wg.vocab.data <- merge(child.source.data, wg.vocab.sizes)
wg.cat.data <- merge(child.source.data, wg.cat.sizes)

ws.vocab.data <- merge(child.source.data, ws.vocab.sizes)
ws.cat.data <- merge(child.source.data, ws.cat.sizes)

wg.age.gender.summary <- wg.vocab.data %>% group_by(gender, age) %>%
  summarise(n = n(),
            productive = mean(productive),
            receptive = mean(receptive))

wg.cat.summary <- wg.cat.data %>% group_by(category) %>%
  summarise(productive = mean(productive),
            receptive = mean(receptive))

wg.age.gender.cat.summary <- wg.cat.data %>% group_by(gender, age, category) %>%
  summarise(productive = mean(productive),
            receptive = mean(receptive))

wg.source.summary <- wg.vocab.data %>% group_by(name) %>%
  summarise(n = n(),
            productive = mean(productive),
            receptive = mean(receptive))

ws.age.gender.summary <- ws.vocab.data %>% group_by(gender, age) %>%
  summarise(n = n(),
            ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))
            
ws.cat.summary <- ws.cat.data %>% group_by(category) %>%
  summarise(ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))

ws.age.gender.cat.summary <- ws.cat.data %>% group_by(gender, age, category) %>%
  summarise(ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))

ws.source.age.cat.summary <- ws.cat.data %>% group_by(name, age, category) %>%
  filter(name != 'Indiana University, Bloomington') %>%
  summarise(ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))

ws.source.summary <- ws.vocab.data %>% group_by(name) %>%
  summarise(n = n(),
            ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))

ws.indiana.age.summary <- ws.vocab.data %>%
  filter(name=="Indiana University, Bloomington") %>%
  group_by(age) %>%
  summarise(n = n(),
            ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            productive = mean(productive))
