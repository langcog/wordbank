library(Hmisc)
library(dplyr)
library(RMySQL)
library(magrittr)

cdiclex <- src_mysql('cdiclex')

corpora <- as.data.frame(tbl(cdiclex, 'cdiclex_corporas'))

vocab_items <- tbl(cdiclex, 'cdi_vocabulary_words') %>%
  select(itemid, corpora, ingroup, native, translation) %>%
  rename(clex_id = itemid,
         group_id = ingroup,
         definition = native,
         gloss = translation)

vocab_groups <- tbl(cdiclex, 'cdi_vocabulary_groups') %>%
  select(id, corpora, translation) %>%
  rename(group_id = id, category = translation)

vocab_config <- tbl(cdiclex, 'cdi_vocabulary_config') %>%
  select(-id)

category_map <- read.csv('clex_category_map.csv', stringsAsFactors = FALSE)
row.names(category_map) <- category_map$clex
category_map %<>% select(-clex)
get_category <- function(clex_category) {
  category_map[clex_category,]
}

# sentences_items <- tbl(cdiclex, 'cdi_sentences_items') %>%
#   select(id, corpora, ingroup, native, translation) %>%
#   rename(clex_id = id,
#          group_id = ingroup,
#          definition = native,
#          gloss = translation)
# 
# sentences_groups <- tbl(cdiclex, 'cdi_sentences_groups') %>%
#   select(id, corpora, translation) %>%
#   rename(group_id = id, category = translation)
# 
# sentences_subjects <- tbl(cdiclex, 'cdi_sentences_subjects') %>%
#   rename(subjectid = id,
#          study_id = originalid)

clean_str <- function(str) {
  no_space <- gsub(" ", "_", gsub(",", "", str))
  gsub("'", "", iconv(no_space, to='ASCII//TRANSLIT'))
}

clean_def <- function(def) {
  gsub("/ ", "/",
       gsub(", ", "/",
            gsub("^ *|(?<= ) | *$", "", def, perl=T)
       )
  )
}

export_corpus <- function(cid) {
  
  corpus <- filter(corpora, id == cid)
  language <- capitalize(corpus$language)
  form <- corpus$text
  if(form == 'Words and Sentences') {form <- 'WS'}
  if(form == 'Words and Gestures') {form <- 'WG'}
  has_vocab <- corpus$vocabularyhasdataset
#  has_sentences <- corpus$sentenceshasdataset
  
  vocab_data <- NULL
  vocab_item_data <- data.frame()
#   sentences_data <- NULL
#   sentences_item_data <- data.frame()
  
  general_field_map <- data.frame(
    field = c("data_age", "sex", "study_id"),
    column = c("month", "sex", "study_id"),
    group = c("admin", "child", "child"),
    type = c("data_age", "sex", "study_id")
  )
  
  if (has_vocab == "true") {
    
    word_choices <- function(form) {
      if (form == "WG") {
        "understands; produces"
      } else {
        "produces"
      }
    }
    
    vocab_item_data <- filter(vocab_items, corpora == cid) %>%
      left_join(vocab_groups) %>%
      select(-corpora, -group_id) %>%
      as.data.frame() %>%
      mutate(item = clean_str(definition),
             type = 'word',
             category = get_category(gsub("\t", "", category)),
             choices = word_choices(form),
             lang_lemma = item,
             uni_lemma = item,
             definition = clean_def(definition),
             gloss = clean_def(gloss),
             lexical_category = "",
             complexity_category = "")
    
    vocab_data <- tbl(cdiclex, paste0('cdi_vocabulary_dataset_', cid)) %>%
      rename(study_id = ID) %>%
      as.data.frame()
    
  }
  
#   if (has_sentences == "true") {
#     
#     sentences_item_data <- filter(sentences_items, corpora == cid) %>%
#       left_join(sentences_groups) %>%
#       select(-corpora, -group_id) %>%
#       as.data.frame() %>%
#       mutate(item = clean_str(definition),
#              type = category,
#              category = category,
#              choices = "",
#              lang_lemma = item,
#              uni_lemma = item,
#              definition = clean_def(definition),
#              gloss = clean_def(gloss),
#              lexical_category = "",
#              complexity_category = "") %>%
#       mutate(clex_id = as.character(clex_id))
#     
#     subj_data <- sentences_subjects %>%
#       filter(corpora == cid) %>%
#       as.data.frame()
#     
#     sentences_data <- tbl(cdiclex, paste0('cdi_sentences_dataset_', cid)) %>%
#       as.data.frame(n = -1) %>%
#       spread(itemid, answer) %>%
#       left_join(subj_data) %>%
#       select(-subjectid, -corpora, -sex, -age)
#     
#   }
  
  instrument <- paste(language, form, sep="_")
  dir.create(paste('clex_data', instrument, sep="/"))
  
#  item_data <- bind_rows(vocab_item_data, sentences_item_data) %>%
  item_data <- vocab_item_data %>%
    mutate(itemID = paste0('item_', row_number()))
  
  item_field_map <- item_data %>%
    rename(field = itemID,
           column = clex_id) %>%
    mutate(group = 'item') %>%
    select(field, column, group, type)
  
  item_data %<>% select(-clex_id)
  
  con_item_data <- file(paste0('clex_data/', instrument, '/', '[', instrument, ']', '.csv'),
                        encoding="utf8")
  write.csv(item_data, file = con_item_data, row.names = FALSE, quote = FALSE)
  
#   if (!is.null(vocab_data) & !is.null(sentences_data)) {
#     data <- inner_join(vocab_data, sentences_data)    
#   } else if (is.null(sentences_data)) {
#     data <- vocab_data  
#   } else if (is.null(sentences_data)) {
#     data <- sentences_data
#   } else {
#     data <- data.frame()
#   }
  
  write.csv(vocab_data,
            paste0('clex_data/', instrument, '/', language, form, '_CLEX_data', '.csv'),
            row.names = FALSE)
  
  field_map <- bind_rows(general_field_map, item_field_map)
  
  write.csv(field_map,
            paste0('clex_data/', instrument, '/', language, form, '_CLEX_fields', '.csv'),
            row.names = FALSE)
  
  config_data <- vocab_config %>%
    filter(corpora == cid) %>%
    as.data.frame()
  
  get_content <- function(value) {
    config_data[config_data$type == value,]$content
  }
  
  sex_value_map <- data.frame(
    type = c('sex', 'sex'),
    value = c('M', 'F'),
    data_value = c(get_content('male'), get_content('female'))
  )
  
  word_value_map <- {
    if (form == 'WS') {
      data.frame(
        type = c('word', 'word'),
        value = c('produces', ''),
        data_value = c(get_content('answer_said'),
                       get_content('answer_non'))
      )
    } else if (form == 'WG') {
      data.frame(
        type = c('word', 'word', 'word'),
        value = c('produces', 'understands', ''),
        data_value = c(get_content('answer_said'),
                       get_content('answer_understood'),
                       get_content('answer_non'))
      )      
    }
  }
  
  value_map <- bind_rows(sex_value_map, word_value_map)
  
  write.csv(value_map,
            paste0('clex_data/', instrument, '/', language, form, '_CLEX_values', '.csv'),
            row.names = FALSE)
  
}

to_export <- c(
  5, #Croatian - Words and Gestures
  6, #Swedish - Words and Gestures
  7, #Swedish - Words and Sentences
  11, #Croatian - Words and Sentences
  12, #German - Words and Sentences
  13, #Italian - Words and Sentences
  15, #Turkish - Words and Gestures
  16, #Russian - Words and Gestures
  17, #Russian - Words and Sentences
  18  #Turkish - Words and Sentences
)

#export_corpus(17)
for (cid in to_export) {
  export_corpus(cid)
}