library(data.table)
library(dplyr)
library(purrr)
library(tidyr)
library(readr)

LANGUAGE <- "Norwegian"
FORM <- "WG"

norming_file <- "Kristoffersen"
other_files <- c("Kristoffersen_longitudinal")


read_data <- function(file) {
  data <- fread(paste0(LANGUAGE, "_", FORM, "/", LANGUAGE, FORM, "_", file, 
               "_data_original.csv"), colClasses = "character", na.strings = "NA") %>%
  #  filter(!is.na(ParticipantId), ParticipantId != "") %>% #English
    filter(!is.na(ID_CDI), ID_CDI != "")# %>%
   # unite(id_age, ParticipantId, CDIAge, remove = FALSE)
  
  data$file = file
  
  return(data)
  
}

write_data <- function(df) {
  file = unique(df$file)
  
  write_csv(select(df, -file), paste0(LANGUAGE, "_", FORM, "/", LANGUAGE, FORM, 
            "_", file, "_data.csv"))
}


norming_data <- read_data(norming_file)

norming_ids <- norming_data %>%
 # select(id_age) %>%
  select(ID_CDI) %>%
  distinct()

other_data <- map(other_files, read_data) 

other_ids <- other_data %>%
#  map(function(df) select(df, id_age)) %>%
  map(function(df) select(df, ID_CDI)) %>%
  bind_rows()

duplicated_ids <- intersect(norming_ids, other_ids)

fixed_norming <- norming_data %>%
  # filter(!id_age %in% duplicated_ids$id_age) %>%
  # select(-id_age) 
  filter(!ID_CDI %in% duplicated_ids$ID_CDI) #%>%
  #select(-id_age) 
  

fixed_norming$norming = TRUE

write_data(fixed_norming)

fix_other_data <- function(df) {
  
  df[, "norming"] = df[,ID_CDI %in% duplicated_ids$ID_CDI]
  
  return(df)
#  df[, "norming"] = df[,id_age %in% duplicated_ids$id_age]
  
#  select(df, -id_age)
}

fixed_other <- other_data %>%
  map(fix_other_data) %>%
  map(write_data)


