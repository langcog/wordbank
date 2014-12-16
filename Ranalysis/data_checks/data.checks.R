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
wordbank <- src_mysql(dbname='wordbank')

#wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
#                      user="wordbank",password="wordbank")

# load all tables
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
instruments.table <- tbl(wordbank,"common_instrumentsmap")
source.table <- tbl(wordbank,"common_source")
wordinfo.table <- tbl(wordbank,"common_wordinfo")
wordmapping.table <- tbl(wordbank,"common_wordmapping")
ws.table <- tbl(wordbank,"instruments_english_ws")
wg.table <- tbl(wordbank,"instruments_english_wg")

ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       item_baa_baa:item_then)) %>%
  rename(id = basetable_ptr_id) %>% # Rename the id
  gather(word,score,item_baa_baa:item_then) %>% # Arrange in longform
  mutate(word = str_replace(word, "item_", "")) # Strip off item_ from words
ws.vocab.words <- mutate(ws.vocab.words, produces = score == 'produces')
ws.vocab.words <- as.tbl(ws.vocab.words)

ws.scores <- as.tbl(ws.vocab.words %>%
                      group_by(id) %>% # Group by child
                      summarise(productive = na.sum(produces))) # Compute productive vocabulary
admins <- admin.table %>%
  select(data_id,child_id,age,data_age,source_id) %>%
  rename(id = data_id, child.id = child_id,source.id = source_id) 
admins <- as.data.frame(admins)

demos <- select(child.table,study_id,id,sex,mom_ed,birth_order) %>%
  rename(child.id = id) # Rename id fields
demos <- as.data.frame(demos)

# Join age and demographics together
child.data <- as.tbl(left_join(admins,demos))
sources <- select(source.table,id,name,dataset,instrument) %>%
  rename(source.id = id,
         source.name = name,
         source.dataset = dataset,
         source.instrument = instrument)
sources <- as.data.frame(sources)
child.data <- as.tbl(left_join(child.data, sources))

ws.data <- left_join(ws.scores, child.data) %>%
  filter(source.name == 'Marchman',
         source.dataset == 'Norming',
         source.instrument == 'English_WS') %>%
  select(-child.id,-source.id) #drop redundant columns
ws.data <- mutate(ws.data, age.check = age==data_age)

productive.vocab <- ws.data %>%
  group_by(age,sex) %>%
  summarise(
    mean = mean(productive),    
    median = median(productive),
    ci.l = ci.low(productive),
    ci.h = ci.high(productive),
    n = n())
