# clear all previous variables
rm(list=ls())

# set path to script folder
setwd('~/Documents/projects/wordbank/Ranalysis')

#load libraries for data manipulation and graphing
library(ggplot2)
library(directlabels)
library(dplyr)
library(reshape2)
library(RSQLite)
library(RSQLite.extfuns)
library(RMySQL)

# set script parameters
instrument = 'wg'
#instrument = 'ws'
#metric.type = 'comprehension'
metric.type = 'production'

# connect to local databse
wordbank <- src_sqlite('wordbank.sqlite')
wordbank <- src_mysql(dbname='wordbank')
#wordbank <- src_mysql(dbname='wordbank',host="54.200.250.120", 
#                      user="wordbank",password="wordbank")

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

# load vocabulary data for chosen instrument
if (instrument == 'ws') {
  vocab.words <- as.data.frame(select(ws.table,
                                      basetable_ptr_id,col_baabaa:col_connthen))
} else if (instrument == 'wg') {
vocab.words <- as.data.frame(select(wg.table,
                                    basetable_ptr_id,col_baabaa:col_some))
}
names(vocab.words)[1] <- "id"

# arrange vocab data by kid and word
kid.words <- melt(vocab.words,
                  id.vars="id",
                  variable.name = "word",
                  value.name = "score")
if (instrument == 'wg') {
  kid.words = mutate(kid.words, 
                    understands = score >= 1,
                    produces = score == 2)
}
if (instrument == 'ws') {
  kid.words = mutate(kid.words, 
                     understands = score == 1,
                     produces = score == 1)
}
kid.words <- arrange(kid.words, id)
kid.words <- mutate(kid.words,
                    lemma = substr(word, 5, length(word)))

# load cdi category information
word.info <- as.data.frame(wordinfo.table)
cdi.cat <- as.data.frame(cdicat.table)
names(cdi.cat)[1] <- "CDI_cat_id"
names(cdi.cat)[2] <- "category"

categorize <- function(cat){
  if (cat == 'sounds') {return ('other')}
  else if (cat == 'animals') {return ('nouns')}
  else if (cat == 'vehicles') {return ('nouns')}
  else if (cat == 'toys') {return ('nouns')}
  else if (cat == 'food_drink') {return ('nouns')}
  else if (cat == 'clothing') {return ('nouns')}
  else if (cat == 'body_parts') {return ('nouns')}
  else if (cat == 'household') {return ('nouns')}
  else if (cat == 'rooms_furn') {return ('nouns')}
  else if (cat == 'outside') {return ('nouns')}
  else if (cat == 'places') {return ('other')}
  else if (cat == 'people') {return ('other')}
  else if (cat == 'games_routines') {return ('other')}
  else if (cat == 'action_words') {return ('predicates')}
  else if (cat == 'descriptive') {return ('predicates')}
  else if (cat == 'time') {return ('other')}
  else if (cat == 'pronouns') {return ('function words')}
  else if (cat == 'question_words') {return ('function words')}
  else if (cat == 'locations') {return ('function words')}
  else if (cat == 'quantifiers') {return ('function words')}
  else if (cat == 'helping_verbs') {return ('function words')}
  else if (cat == 'connecting_words') {return ('function words')}
}

cat <- cdi.cat %>%
  group_by(category) %>%
  mutate(lex.cat = categorize(category))

word.cats <- merge(word.info, cat)
kid.word.data <- merge(kid.words, word.cats)
kid.word.data <- arrange(kid.word.data, id)

form.cat.sizes <- word.cats %>%
  group_by(lex.cat) %>%
  summarise(num.cat = n())
total <- sum(form.cat.sizes$num.cat)
form.cat.sizes <- mutate(form.cat.sizes,
                         prop.cat = num.cat / total)

kids = group_by(kid.word.data, id)
kids.categories = group_by(kid.word.data, id, lex.cat)
if (metric.type == 'production') {
  vocab.sizes = summarise(kids, vocab.size = sum(produces == 1))
  category.sizes = summarise(kids.categories, category.size = sum(produces == 1))
} else if (metric.type == 'comprehension') {
  vocab.sizes = summarise(kids, vocab.size = sum(understands == 1))
  category.sizes = summarise(kids.categories, category.size = sum(understands == 1))
}

vocab.data <- merge(vocab.sizes, category.sizes)
vocab.data <- filter(vocab.data, vocab.size != 0)
vocab.data <- mutate(vocab.data,
                     percent.vocab = category.size / vocab.size)
vocab.data <- filter(vocab.data, lex.cat != "other")

if(metric.type == 'comprehension') {vocab.type = 'Receptive'}
if(metric.type == 'production') {vocab.type = 'Productive'}

#quartz(width=7,height=6)
ggplot(vocab.data, na.rm=TRUE,
       aes(x=vocab.size, y=percent.vocab,colour=lex.cat, label=lex.cat))+
  geom_point(aes(shape=factor(lex.cat)), size = I(1), alpha = I(0.25)) +
  geom_hline(aes(yintercept=form.cat.sizes$prop.cat[form.cat.sizes$lex.cat == 'nouns']), linetype="dashed", color="grey") +
  geom_hline(aes(yintercept=form.cat.sizes$prop.cat[form.cat.sizes$lex.cat == 'predicates']), linetype="dashed", color="grey") +
  geom_hline(aes(yintercept=form.cat.sizes$prop.cat[form.cat.sizes$lex.cat == 'function words']), linetype="dashed", color="grey") +
  geom_smooth(aes(group=lex.cat), method='loess', span=0.5) +
  scale_colour_discrete(breaks=c("nouns", "predicates", "function words"),
                        name="Lexical Class") +
  scale_x_continuous(name = paste(vocab.type, "Vocabulary Size (words)", sep=" ")) +
  scale_y_continuous(name = "Percentage of total vocabulary") +
  theme(axis.text.x = element_text(angle=-40, hjust = 0),
        axis.title.y = element_text(vjust=0.35),
        axis.title.x = element_text(vjust=-0.5),
        legend.position="none") +
  geom_dl(aes(label=lex.cat), method=list("smart.grid"))

ggsave(file=paste("vocabulary_composition", instrument, metric.type, "pdf", sep="."),
       width=8,height=6)
