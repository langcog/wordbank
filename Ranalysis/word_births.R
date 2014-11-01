############## STUFF THAT RUNS ONCE WHEN APP LOADS ##############
library(ggplot2)
library(dplyr)
library(tidyr)
library(RMySQL)

## OPEN DATABASE CONNECTION ##
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")

ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_connthen)) %>%
  rename(id = basetable_ptr_id) %>% # Rename the id
  gather(word,produces,col_baabaa:col_connthen) %>% # Arrange in longform
  mutate(word = str_replace(word, "col_", "")) # Strip off col_ from words

ws.vocab.words <- as.tbl(ws.vocab.words)

admins <- admin.table %>%
  select(data_id,child_id,age,source_id) %>%
  rename(id = data_id, child.id = child_id,source.id = source_id) 
admins <- as.data.frame(admins)

# Get demographic variables for each child
demos <- select(child.table,id,gender,mom_ed,birth_order) %>%
  rename(child.id = id) # Rename id fields
demos <- as.data.frame(demos)

# Join age and demographics together
child.data <- as.tbl(left_join(admins,demos))

# filter down
ws.data <- left_join(ws.vocab.words, child.data) %>%
  filter(age >= 16, age <= 30) %>%
  select(-child.id,-source.id) #drop redundant columns

word.births <- ws.data %>%
  group_by(age,word) %>% 
  summarise(prop = mean(produces))

qplot(age, prop, col=word, geom="line", group=word, 
      data=word.births)

aoas <- word.births %>%
  group_by(word) %>%
  summarise(aoa = age[prop > .50][1]) %>%
  arrange(aoa) %>%
  filter(!is.na(aoa)) 

qplot(aoa, data=aoas)

### get kuypermans data
library(data.table)
preds <- fread("~/Projects/Wordbank/wordbank/Ranalysis/AoA_ratings_Kuperman_et_al_BRM.csv")
preds <- preds %>% rename(word = Word)

## merge
aoas.preds <- inner_join(aoas, preds, by="word")

ggplot(aoas.preds, aes(x=aoa, y=Rating.Mean, label=word)) + 
  geom_smooth(method="lm") + 
  geom_text(size=3)

ggplot(aoas.preds, aes(x=aoa, y=log(Freq_pm), label=word)) + 
  geom_smooth(method="lm") + 
  geom_text(size=3)



## regression
lm(aoa ~ log(Freq_pm) + 

