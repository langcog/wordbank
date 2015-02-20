library(dplyr)
library(tidyr)
library(RMySQL)
library(ggplot2)
library(microbenchmark)
setwd("~/Documents/projects/wordbank/scripts/benchmarking")

wordbank.local <- src_mysql(dbname='wordbank')
#wordbank.remote <- src_mysql(dbname="wordbank", host="54.149.39.46",
#                             user="wordbank", password="wordbank")

# load tables
#source.table <- tbl(wordbank, "common_source")
admin.table <- tbl(wordbank.local, "common_administration")
child.table <- tbl(wordbank.local, "common_child")
wordmapping.table <- tbl(wordbank.local, "common_wordmapping")
instruments.table <- tbl(wordbank.local, "common_instrumentsmap")

english.ws.table.local <- tbl(wordbank.local, "instruments_english_ws")
english.wg.table.local <- tbl(wordbank.local, "instruments_english_wg")
spanish.ws.table.local <- tbl(wordbank.local, "instruments_spanish_ws")
spanish.wg.table.local <- tbl(wordbank.local, "instruments_spanish_wg")
norwegian.ws.table.local <- tbl(wordbank.local, "instruments_norwegian_ws")
norwegian.wg.table.local <- tbl(wordbank.local, "instruments_norwegian_wg")
danish.ws.table.local <- tbl(wordbank.local, "instruments_danish_ws")

#english.ws.table.remote <- tbl(wordbank.remote, "instruments_english_ws")
#english.wg.table.remote <- tbl(wordbank.remote, "instruments_english_wg")
#spanish.ws.table.remote <- tbl(wordbank.remote, "instruments_spanish_ws")
#spanish.wg.table.remote <- tbl(wordbank.remote, "instruments_spanish_wg")
#norwegian.ws.table.remote <- tbl(wordbank.remote, "instruments_norwegian_ws")
#norwegian.wg.table.remote <- tbl(wordbank.remote, "instruments_norwegian_wg")
#danish.ws.table.remote <- tbl(wordbank.remote, "instruments_danish_ws")

# get administration info
admins <- admin.table %>%
  select(data_id,child_id,age,source_id) %>%
  rename(id = data_id, child.id = child_id, source.id = source_id) %>%
  transform(id = as.numeric(id))
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
  
#  t <- Sys.time()
  
  instrument.items <- items %>% 
    filter(language == instrument.language, form == instrument.form) %>%
    select(item_id, item, type, category, lexical_category, definition, complexity_category) %>%
    mutate(item_id = as.numeric(substr(item_id, 6, nchar(item_id))))
    
#  print(paste("instrument.items", Sys.time()-t))
#  t <- Sys.time()
  
  columns <- colnames(instrument.table)
  instrument.names <- columns[2:length(columns)]

#  print(paste("instrument.names", Sys.time()-t))
#  t <- Sys.time()
    
  instrument.data <- as.data.frame(instrument.table) %>%
    transform(id = as.numeric(basetable_ptr_id)) %>%
    gather_("item_id", "value", instrument.names, convert=TRUE) %>%
    mutate(item_id = as.numeric(substr(item_id, 6, nchar(item_id))))

#  print(paste("instrument.data", Sys.time()-t))
#  t <- Sys.time()

  d <- left_join(instrument.data, instrument.items, by=c("item_id"))
  
#  print(paste("instrument.data + instrument.items", Sys.time()-t))
#  t <- Sys.time()

  d <- left_join(d, child.data, by=c("id"))
  
#  print(paste("instrument.data + instrument.items + child.data", Sys.time()-t))

return(d)
}

data.loading.time <- function(table, language, form) {
  start <- Sys.time()
  data <- get.instrument.data(table, language, form)
  end <- Sys.time()
return(end-start)
}

expr <- c("EnglishWS", "EnglishWG", "SpanishWS", "SpanishWG", "NorwegianWS", "NorwegianWG", "DanishWS")
n <- c(nrow(english.ws.table.local), nrow(english.wg.table.local),
       nrow(spanish.ws.table.local), nrow(spanish.wg.table.local),
       nrow(norwegian.ws.table.local), nrow(norwegian.wg.table.local),
       nrow(danish.ws.table.local))
ns <- data_frame(expr, n)

local <- microbenchmark(EnglishWS = get.instrument.data(english.ws.table.local, "English", "WS"),
                        EnglishWG = get.instrument.data(english.wg.table.local, "English", "WG"),
                        SpanishWS = get.instrument.data(spanish.ws.table.local, "Spanish", "WS"),
                        SpanishWG = get.instrument.data(spanish.wg.table.local, "Spanish", "WG"),
                        NorwegianWS = get.instrument.data(norwegian.ws.table.local, "Norwegian", "WS"),
                        NorwegianWG = get.instrument.data(norwegian.wg.table.local, "Norwegian", "WG"),
                        DanishWS = get.instrument.data(danish.ws.table.local, "Danish", "WS"),
                        times=10)

#remote <- microbenchmark(EnglishWS = get.instrument.data(english.ws.table.remote, "English", "WS"),
#                        EnglishWG = get.instrument.data(english.wg.table.remote, "English", "WG"),
#                        SpanishWS = get.instrument.data(spanish.ws.table.remote, "Spanish", "WS"),
#                        SpanishWG = get.instrument.data(spanish.wg.table.remote, "Spanish", "WG"),
#                        NorwegianWS = get.instrument.data(norwegian.ws.table.remote, "Norwegian", "WS"),
#                        NorwegianWG = get.instrument.data(norwegian.wg.table.remote, "Norwegian", "WG"),
#                        DanishWS = get.instrument.data(danish.ws.table.remote, "Danish", "WS"), times=10)
  
#times10 <- left_join(local, remote, by=c("expr")) %>%
#  rename(local = time.x, remote = time.y) %>%
#  gather(type, time, local, remote) %>%
#  mutate(time = time*1e-09)

#times10_n <- left_join(times10, ns)
times_n <- left_join(local, ns) %>%
  mutate(time = time*1e-09)

write.csv(times_n, "benchmarking.csv")

ggplot(times_n, aes(x=n, y=time), color=type) +
  geom_point() + 
  geom_smooth() +
  theme_bw()
ggsave("local_benchmark.png")
