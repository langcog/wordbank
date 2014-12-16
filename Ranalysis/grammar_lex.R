library(ggplot2)
library(dplyr)
library(tidyr)
library(RMySQL)
library(stringr)

## OPEN DATABASE CONNECTION ##
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

## NOW LOAD TABLES ##
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")

## BREAK OUT THE ITEMS -----------------
ws.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_connthen)) %>%
  rename(id = basetable_ptr_id) %>% # Rename the id
  gather(word,produces,col_baabaa:col_connthen) %>% # Arrange in longform
  mutate(word = str_replace(word, "col_", "")) %>% # Strip off col_ from words
  group_by(id) %>%
  summarise(vocab = sum(produces))

ws.syntax <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_complx01:col_complx37)) %>%
  rename(id = basetable_ptr_id) %>% # Rename the id
  gather(word,produces,col_complx01:col_complx37) %>% # Arrange in longform
  mutate(word = str_replace(word, "col_", "")) %>% # Strip off col_ from words
  group_by(id) %>%
  summarise(syntax = mean(produces))

ws.morpho <- as.data.frame(select(ws.table,
                                        basetable_ptr_id,
                                        col_splural:col_ed, 
                                        col_children:col_went)) %>%
  rename(id = basetable_ptr_id) %>% # Rename the id
  gather(word,produces,col_splural:col_went) %>% # Arrange in longform
  mutate(word = str_replace(word, "col_", "")) %>% # Strip off col_ from words
  group_by(id) %>%
  summarise(morpho = mean(produces))

### MERGE OTHER ------------
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

# join variables
ws.sums <- left_join(ws.words, ws.syntax)
ws.sums <- left_join(ws.sums, ws.morpho)

# filter down
d <- left_join(ws.sums, child.data) %>%
  filter(syntax > 0, vocab > 0, morpho > 0, 
         age > 15 & age < 35) %>%
  select(-child.id,-source.id) %>% #drop redundant columns 
  mutate(age_binned = cut(age, breaks = c(15, 20, 25, 30, 35)))

### PLOTS --------------
ms <- d %>% gather(measure, score, syntax:morpho)
levels(ms$measure) <- c("Syntax","Morphology")
#quartz()
qplot(vocab, score, col = age_binned, 
      data = ms) + 
  geom_smooth(method="lm", formula = y ~ I(x^2) - 1) + 
  facet_wrap(~measure) + 
  xlim(c(0,680)) + 
  ylim(c(0, 1)) + 
  xlab("Vocabulary (WS)") + 
  ylab("Score (Mean Items)")



### make these two facets
qplot(vocab, syntax, col=age_binned, 
      data=d) + 
  geom_smooth(se=FALSE) + 
  ylim(c(0, 37))

qplot(vocab, morpho, col=age_binned, 
      data=d) + 
  geom_smooth() + 
  ylim(c(0, 33))

d$s.vocab <- scale(d$vocab)
d$s.age <- scale(d$age)

summary(lm(syntax ~ I(vocab^2) * age - 1, data=d))
summary(lm(morpho ~ I(vocab^2) * age - 1, data=d))

summary(lm(syntax ~ I(d$s.vocab^2) * d$age_bin - 1, data=d))
summary(lm(morpho ~ I(d$s.vocab^2) * d$age_bin - 1, data=d))

