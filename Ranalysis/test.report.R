# clear all previous variables
rm(list=ls())

#get lab version of useful R functions
source('../Other/Ranalysis/useful.R')

#load libraries for data manipulation and graphing
library(directlabels)
library(data.table)
library(dplyr)

# connect to local databse
wordbank <- src_mysql(dbname='wordbank')

# load all tables
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
instruments.table <- tbl(wordbank,"common_instrumentsmap")
source.table <- tbl(wordbank,"common_source")
wordinfo.table <- tbl(wordbank,"common_wordinfo")
mapping.table <- tbl(wordbank,"common_wordmapping")
wg.table <- tbl(wordbank,"instruments_wg")
ws.table <- tbl(wordbank,"instruments_ws")

vocab.words <- as.data.frame(select(wg.table,id:col_some))
bykid.longform <- melt(vocab.words,id.vars="id",variable.name = "word",
                       value.name="produces")

production.scores <- bykid.longform %.%
  group_by(id) %.%
  summarise(productive = sum(produces == 2))

admins <- as.data.frame(admin.table %.%
                          select(data_id,child_id,age) %.%
                          filter(age < 99))
children <- as.data.frame(select(child.table,id,gender))
names(children)[1] <- "child.id"
names(admins)[1:2] <- c("id","child.id")

child.data <- merge(children,admins,production.scores)

child.data <- merge(child.data,production.scores)

momed.gender.data <- child.data %.%
  select(child.id:productive) %.%
  filter(age >= 9 & age < 99) %.%
  group_by(age,gender) %.%
  summarise(vocab = mean(productive),
            ci.h = ci.high(productive),
            ci.l = ci.low(productive),
            n = n())


quartz(width=7,height=4)
ggplot(age.gender.data, 
       aes(x=age, y=vocab,colour=gender,label=gender,fill=gender))+
  geom_pointrange(aes(ymin = vocab-ci.l,
                      ymax = vocab+ci.h),
                  size = .8) +
  geom_line(size=1) +
  scale_x_continuous(breaks=seq(9,18,1),
                     name = "MomEd")+
  scale_y_continuous(name = "Productive Vocabulary Size (words)") +
  theme_bw(base_size=14) + 
  theme(legend.position="none") +
  geom_dl(method=list("last.qp",cex=1,hjust=-.5)) 
  
quartz()
plot(hist(production.scores$productive))
