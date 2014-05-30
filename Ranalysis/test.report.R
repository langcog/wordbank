# clear all previous variables
rm(list=ls())

#get lab version of useful R functions
source('~/Projects/Other/Ranalysis/useful.R')

#load libraries for data manipulation and graphing
library(directlabels)
library(dplyr)

# connect to local databse
wordbank <- src_sqlite('wordbank.sqlite')

# load all tables
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
instruments.table <- tbl(wordbank,"common_instrumentsmap")
source.table <- tbl(wordbank,"common_source")
wordinfo.table <- tbl(wordbank,"common_wordinfo")
mapping.table <- tbl(wordbank,"common_wordmapping")
ws.table <- tbl(wordbank,"instruments_ws")

vocab.words <- as.data.frame(select(ws.table,
                                    col_baabaa:col_connthen,basetable_ptr_id))
bykid.longform <- melt(vocab.words,id.vars="basetable_ptr_id",
                       variable.name = "word",
                       value.name="produces")

production.scores <- bykid.longform %>%
  group_by(basetable_ptr_id) %>%
  summarise(productive = sum(produces == 1))
names(production.scores)[1] <- "id"

admins <- as.data.frame(select(admin.table,data_id,child_id,age))
                        
children <- as.data.frame(select(child.table,id,gender,mom_ed,birth_order))
names(children)[1] <- "child.id"
names(admins)[1:2] <- c("id","child.id")

child.data <- merge(children,admins)

child.data <- merge(child.data,production.scores)

age.gender.data <- child.data %>%
  select(child.id:productive) %>%
  group_by(age,gender) %>%
  filter(age <= 30) %>%
  summarise(vocab = na.mean(productive),
            ci.l = ci.low(productive),
            ci.h = ci.high(productive),
            n = n())

quartz(width=7,height=4)
ggplot(age.gender.data, 
       aes(x=age, y=vocab,colour=gender,label=gender,fill=gender))+
  geom_pointrange(aes(ymin = vocab-ci.l,
                      ymax = vocab+ci.h),
                  size = .8) +
  geom_line(size=1) +
  scale_x_continuous(breaks=seq(16,30,1),
                     name = "Age (months)")+
  scale_y_continuous(name = "Productive Vocabulary Size (words)") +
  theme_bw(base_size=14) + 
  theme(legend.position="none") +
  geom_dl(method=list("last.qp",cex=1,hjust=-.5)) 
  
