# clear all previous variables
rm(list=ls())

setwd('~/Documents/projects/wordbank/Ranalysis')

#get lab version of useful R functions
source('~/Documents/projects/Ranalysis/useful.R')

#load libraries for data manipulation and graphing
library(directlabels)
library(dplyr)
library(RSQLite)
library(RSQLite.extfuns)
library(RMySQL)
library(scales)

# connect to local databse
wordbank <- src_sqlite('wordbank.sqlite')
wordbank <- src_mysql(dbname='wordbank')

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

vocab.words <- as.data.frame(select(wg.table,
                                    basetable_ptr_id,col_baabaa:col_some))
names(vocab.words)[1] <- "id"

kid.words <- melt(vocab.words,
                  id.vars="id",
                  variable.name = "word",
                  value.name = "score")
kid.words <- arrange(kid.words, id)
kid.words <- mutate(kid.words,
                    lemma = substr(word, 5, length(word)))
kid.words = mutate(kid.words, 
                   understands = score >= 1,
                   produces = score == 2)

kids <- group_by(kid.words, id)
vocab.sizes <- summarise(kids, vocab.size = sum(produces))
kid.words <- merge(kid.words, vocab.sizes)

admins <- as.data.frame(select(admin.table,data_id,child_id,age,source_id))
children <- as.data.frame(select(child.table,id,gender))
child.data <- merge(children,admins,by.y="child_id",by.x = "id")
kid.word.data <- merge(kid.words, child.data)

word.info <- as.data.frame(wordinfo.table)
cdi.cat <- as.data.frame(cdicat.table)
names(cdi.cat)[1] <- "CDI_cat_id"
names(cdi.cat)[2] <- "category"
word.cat <- merge(word.info, cdi.cat)

kid.word.data <- merge(kid.word.data, word.cat)
kid.word.data <- filter(kid.word.data, lemma != 'mommy')
kid.word.data <- filter(kid.word.data, lemma != 'daddy')

kid.words.young <- filter(kid.word.data, age <= 12)
#kid.words.low <- filter(kid.word.data, vocab.size <= 50)

first.words.young <- kid.words.young %>%
  group_by(lemma) %>%
  summarise(n.kids = n(),
            prop = sum(produces) / n.kids)
first.words.young <- arrange(first.words.young, desc(prop))

first.words.byage <- kid.words.young %>%
  group_by(lemma, age) %>%
  summarise(n.kids = n(),
            prop = sum(produces) / n.kids)
first.words.byage <- merge(first.words.byage, first.words.young, by='lemma')
first.words.byage <- arrange(first.words.byage, desc(prop.y))

first.words.bygender <- kid.words.young %>%
  group_by(lemma, gender) %>%
  summarise(n.kids = n(),
            prop = sum(produces) / n.kids)
first.words.bygender <- merge(first.words.bygender, first.words.young, by='lemma')
first.words.bygender <- arrange(first.words.bygender, desc(prop.y))

first.words.young <- slice(first.words.young, 1:20)
quartz(width=8,height=6)
ggplot(first.words.young, 
  aes(lemma, prop)) +
  geom_bar(stat="identity") +
  scale_x_discrete(limits = first.words.young$lemma,
                   name = "Words&Gestures lemma") +
  scale_y_continuous(name = "Proportion of children producing") +
  theme(axis.text.x = element_text(angle=90, hjust=1, vjust=0.5)) +
  ggtitle("Common words produced by children up to 12 months old")

first.words.byage <- slice(first.words.byage, 1:100)
first.words.byage$age <- factor(first.words.byage$age)
levels(first.words.byage$age) <- c('8 months', '9 months', '10 months', '11 months', '12 months')
quartz(width=11,height=6)
ggplot(first.words.byage, 
  aes(lemma, prop.x, fill=age)) +
#  geom_bar(stat="identity", position="dodge") +
  geom_bar(stat="identity", width=3) +
  facet_grid(~age)+#, scales="free", space="free") +
  scale_x_discrete(limits = first.words.byage$lemma,
                   name = "Words&Gestures lemma") +
  scale_y_continuous(name = "Proportion of children producing") +
  theme(axis.text.x = element_text(angle=90, hjust=1, vjust=0.5, size=7)) +
  scale_fill_discrete(name="Age (months)") +
  guides(fill=FALSE) +
  ggtitle("Common words produced by children up to 12 months old (by age)")

first.words.bygender <- slice(first.words.bygender, 1:40)
first.words.bygender$gender <- factor(first.words.bygender$gender)
levels(first.words.bygender$gender) <- c('Female', 'Male')
quartz(width=10,height=6)
ggplot(first.words.bygender, 
       aes(lemma, prop.x, fill=gender)) +
  geom_bar(stat="identity", width=1.2) +
  facet_grid(~gender, scales="free", space="free") +
  scale_x_discrete(limits = first.words.bygender$lemma,
                   name = "Words&Gestures lemma") +
  scale_y_continuous(name = "Proportion of children producing") +
  theme(axis.text.x = element_text(angle=90, hjust=1, vjust=0.5)) +
  scale_fill_discrete(name="Gender") +
  guides(fill=FALSE) +
  ggtitle("Common words produced by children up to 12 months old (by gender)")
