rm(list=ls())

library(dplyr)
library(tidyr)
library(RMySQL)
library(magrittr)

wordbank <- src_mysql(dbname='wordbank')
#wordbank <- src_mysql(dbname="wordbank", host="54.149.39.46",
#                      user="wordbank", password="wordbank")

# load tables
#source.table <- tbl(wordbank, "common_source")
admin.table <- tbl(wordbank, "common_administration")
child.table <- tbl(wordbank, "common_child")
wordmapping.table <- tbl(wordbank, "common_wordmapping")
instruments.table <- tbl(wordbank, "common_instrumentsmap")
english.ws.table <- tbl(wordbank, "instruments_english_ws")
english.wg.table <- tbl(wordbank, "instruments_english_wg")
spanish.ws.table <- tbl(wordbank, "instruments_spanish_ws")
spanish.wg.table <- tbl(wordbank, "instruments_spanish_wg")
norwegian.ws.table <- tbl(wordbank, "instruments_norwegian_ws")
norwegian.wg.table <- tbl(wordbank, "instruments_norwegian_wg")
danish.ws.table <- tbl(wordbank, "instruments_danish_ws")

# get administration info
admins <- admin.table %>%
  select(data_id,child_id,age,source_id) %>%
  rename(id = data_id, child.id = child_id, source.id = source_id) 
child.data <- as.data.frame(admins)

# get word mapping info
mapping <- as.data.frame(wordmapping.table)

# get instrument info
instruments <- as.data.frame(instruments.table) %>%
  rename(instrument_id = id)

# join items and instruments together
items <- left_join(mapping, instruments) %>%
  mutate(language = factor(language, levels = c("Norwegian", "English", "Danish", "Spanish")))


get.instrument.data <- function(instrument.table, instrument.language, instrument.form) {
  
  instrument.items <- items %>% 
    filter(language == instrument.language, form == instrument.form) %>%
    select(item_id, item, type, category, lexical_category, definition, complexity_category) %>%
    mutate(item_id = as.numeric(str_replace(item_id, "item_", "")))
  
  columns <- colnames(instrument.table)
  instrument.names <- columns[2:length(columns)]
  
  instrument.data <- as.data.frame(instrument.table) %>%
    rename(id = basetable_ptr_id) %>%
  # gather(item, value, -id) %>%
    gather_("item_id", "value", instrument.names) %>%
    mutate(item_id = as.numeric(str_replace(item_id, "item_", "")))
  
  d <- left_join(instrument.data, instrument.items, by=c("item_id"))
  
  d <- left_join(d, child.data)
  return(d)
}

data.loading.time <- function(table, language, form) {
  start <- Sys.time()
  data <- get.instrument.data(table, language, form)
  end <- Sys.time()
return(end-start)
}


language <- c("English", "English", "Spanish", "Spanish", "Norwegian", "Norwegian", "Danish")
form <- c("WS", "WG", "WS", "WG", "WS", "WG", "WS")
n <- c(nrow(english.ws.table), nrow(english.wg.table),
       nrow(spanish.ws.table), nrow(spanish.wg.table),
       nrow(norwegian.ws.table), nrow(norwegian.wg.table),
       nrow(danish.ws.table))
time <- c(data.loading.time(english.ws.table, "English", "WS"),
          data.loading.time(english.wg.table, "English", "WG"),
          data.loading.time(spanish.ws.table, "Spanish", "WS"),
          data.loading.time(spanish.wg.table, "Spanish", "WG"),
          data.loading.time(norwegian.ws.table, "Norwegian", "WS"),
          data.loading.time(norwegian.wg.table, "Norwegian", "WG"),
          data.loading.time(danish.ws.table, "Danish", "WS"))

times <- data_frame(language, form, n, time)

ggplot(times, aes(x=n, y=time)) +
  geom_point()