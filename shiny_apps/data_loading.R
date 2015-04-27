library(dplyr)
library(tidyr)
library(RMySQL)
library(assertthat)


# Takes a connection mode: one of local, prod, or dev
# Returns a connection to the Wordbank MySQL database created with src_mysql
connect.to.wordbank <- function(mode) {
  
  assert_that(is.element(mode, c("local", "prod", "dev")))
  address <- switch(mode,
                    local = "",
                    prod = "54.200.225.86",
                    dev = "54.149.39.46")
  
  con <- src_mysql(host=address, dbname="wordbank", user="wordbank", password="wordbank")
  return(con)
}

# Takes a connection to a MySQL database created with src_mysql
# Pulls all of the common tables
# Returns a list whose names are the names of the tables and whose values
# are tbls
#
# Example:
# wordbank <- src_mysql(dbname="wordbank", host="54.149.39.46",
#                       user="wordbank", password="wordbank")
# common.tables <- get.common.tables(wordbank)
get.common.tables <- function(db) {
  
  names <- Filter(function(tbl) substr(tbl, 1, 7) == "common_", src_tbls(db))
  
  tables <- sapply(names, function(name) tbl(db, name), simplify=FALSE)
  names(tables) <- sapply(names(tables), function(name) substr(name, 8, nchar(name)),
                          simplify=FALSE)
  
  return(tables)
}


# Takes a connection to a MySQL database created with src_mysql and the instrumentsmap
# Loads all of the instruments in the instrumentsmap
# Returns a dataframe whose rows are individual instruments and 
# whose $table column is the corresponding tbl
get.instrument.tables <- function(db, instrumentsmap) {
  
  instrument.tables <- as.data.frame(instrumentsmap) %>%
    mutate(table.name = paste("instruments", tolower(language), tolower(form), sep = "_")) %>%
    rename(instrument_id = id) %>%
    group_by(instrument_id, language, form, age_min, age_max, has_grammar) %>%
    do(table = tbl(db, .$table.name))
  
  return(instrument.tables)
  
}

# Takes in all of the tables that correspond to demographics about administrations
# Returns a dataframe in which each row is one administration and 
# each column is a demographic variable
get.administration.data <- function(momed.table, child.table, instruments.table, admin.table) {
  
  mom_ed <- as.data.frame(momed.table) %>%
    rename(momed_id = id, momed.level = level, momed.order = order) %>%
    arrange(momed.order) %>%
    mutate(momed_id = as.numeric(momed_id),
           momed.level = factor(momed.level, levels = momed.level))
  
  children <- as.data.frame(child.table) %>%
    select(id, birth_order, ethnicity, sex, momed_id) %>%
    rename(child_id = id, birth.order = birth_order) %>%
    mutate(child_id = as.numeric(child_id),
           momed_id = as.numeric(momed_id)) %>%
    left_join(mom_ed) %>%
    select(-momed_id)
  
  instruments <- as.data.frame(instruments.table) %>%
    rename(instrument_id = id) %>%
    mutate(instrument_id = as.numeric(instrument_id))
  
  admins <- as.data.frame(admin.table) %>%
    select(data_id, child_id, age, instrument_id, comprehension, production) %>%
    mutate(data_id = as.numeric(data_id),
           child_id = as.numeric(child_id)) %>%
    left_join(instruments) %>%
    select(-instrument_id) %>%
    left_join(children) %>%
    select(-child_id) %>%
    filter(age >= age_min, age <= age_max)
  
  return(admins)
  
}


# Gets by-item data from an instrument with information from the wordmapping table
get.item.data <- function(wordmapping.table, instruments.table, categories.table) {
  
  instruments <- as.data.frame(instruments.table) %>%
    rename(instrument_id = id)
  
  categories <- as.data.frame(categories.table) %>%
    rename(category_id = id,
           category = name)
  
  items <- as.data.frame(wordmapping.table) %>%
    rename(item.id = item_id) %>%
    left_join(instruments) %>%
    left_join(categories)
  
  return(items)
  
}


# Takes an instrument table and a list of columns
# Selects those columns from the instrument table and gathers them into 
# administration x item form
get.instrument.data <- function(instrument.table, columns) {
  
  instrument.data <- instrument.table %>%
    select(basetable_ptr_id, one_of(columns)) %>%
    as.data.frame %>%
    mutate(data_id = as.numeric(basetable_ptr_id)) %>%
    select(-basetable_ptr_id) %>%
    gather_("item_id", "value", columns, convert = TRUE) %>%
    mutate(item.id = as.numeric(substr(item_id, 6, nchar(item_id)))) %>%
    select(-item_id) %>%
    mutate(value = ifelse(is.na(value), "", value)) %>%
    arrange(data_id)
  
  return(instrument.data)
}
