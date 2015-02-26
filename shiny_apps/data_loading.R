library(dplyr)
library(tidyr)
library(RMySQL)

get.instrument.tables <- function(instruments.table) {
  
  instrument.tables <- as.data.frame(instruments.table) %>%
    mutate(table.name = paste("instruments", tolower(language), tolower(form), sep="_")) %>%
    rename(instrument_id = id) %>%
    group_by(instrument_id, language, form) %>%
    do(table = tbl(wordbank, .$table.name))
  
  return(instrument.tables)
  
}

get.administration.data <- function(momed.table, child.table, instruments.table, admin.table) {
  
  mom_ed <- as.data.frame(momed.table) %>%
    rename(momed_id = id, momed.level = level, momed.order = order)
  
  children <- as.data.frame(child.table) %>%
    select(id, birth_order, ethnicity, sex, momed_id) %>%
    rename(child_id = id, birth.order = birth_order) %>%
    left_join(mom_ed) %>%
    select(-momed_id)
  
  instruments <- as.data.frame(instruments.table) %>%
    rename(instrument_id = id)
  
  admins <- as.data.frame(admin.table) %>%
    select(data_id, child_id, age, instrument_id, comprehension, production) %>%
    rename(admin.id = data_id) %>%
    left_join(instruments) %>%
    select(-instrument_id) %>%
    left_join(children) %>%
    select(-child_id)
  
  return(admins)
  
}

get.item.data <- function(wordmapping.table, instruments.table) {
  
  instruments <- as.data.frame(instruments.table) %>%
    rename(instrument_id = id)
  
  items <- as.data.frame(wordmapping.table) %>%
    #    mutate(item.id = as.numeric(substr(item_id, 6, nchar(item_id)))) %>%
    #    select(-item_id) %>%
    rename(item.id = item_id) %>%
    left_join(instruments)
  
  return(items)
  
}

get.instrument.data <- function(instrument.table, columns) {
  
  instrument.data <- instrument.table %>%
    select(basetable_ptr_id, one_of(columns)) %>%
    as.data.frame %>%
    mutate(admin.id = as.numeric(basetable_ptr_id)) %>%
    select(-basetable_ptr_id) %>%
    gather_("item_id", "value", columns, convert=TRUE) %>%
    mutate(item.id = as.numeric(substr(item_id, 6, nchar(item_id)))) %>%
    select(-item_id) %>%
    mutate(value = ifelse(is.na(value), "", value)) %>%
    mutate(produces = value == 'produces',
           understands = value == 'understands' | value == 'produces') %>%
    select(-value) %>%
    gather(measure, value, produces, understands)
  
  return(instrument.data)
  
}