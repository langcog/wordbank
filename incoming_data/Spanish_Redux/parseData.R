library(tidyverse)
library(readxl)
library(lubridate)

raw_items <- read_csv("incoming_data/Spanish_Redux/spantoditemsbysub.csv") %>%
  select(-id_1, -months_1) %>%
  filter(row_number() > 1) %>%
  mutate(id = as.numeric(as.character(id))) %>%
  rename(birthord_1 = birthord, cdiage_1 = cdiage, sex_1 = sex)

raw_combine <- read_excel("incoming_data/Spanish_Redux/combinemomed.xlsx") %>%
  select(-MotherEd) %>%
  rename(id = ParticipantId, birthord_2 = BOrder, cdiage_2 = CDIAge, combine_1 = COMBINE)

raw_usewords <- read_excel("incoming_data/Spanish_Redux/spanwordformshowuse.xlsx") %>%
  rename(id = ParticipantId, cdiage_3 = CDIAge) %>%
  rename_all(funs(tolower))

raw_grammar <- read_excel("incoming_data/Spanish_Redux/SpanWSgrammaritemdata.xlsx") %>%
  select(-contains("X__")) %>%
  rename(id = ParticipantId, cdiage_4 = CDIAge, sex_2 = Gender, combine_2 = SCOMBINE) %>%
  rename_all(funs(tolower))

merged_data <- raw_items %>%
  full_join(raw_combine) %>%
  full_join(raw_usewords) %>%
  full_join(raw_grammar) %>%
  select(id, dob, cdidate, months, sex_1, 
         birthord_1, momsed, prematur, am:y, combine_1, 
         iacaba:useposs, scmplx01:scmplx37) %>%
  rename(combine = combine_1, sex = sex_1, birthord = birthord_1) %>%
  mutate(data_age = floor(as.numeric(parse_date(cdidate, "%Y-%m-%d") - parse_date(dob, "%Y-%m-%d"), units = "days")/(365.2425/12))) %>%
  select(id, cdidate, data_age, months, sex:scmplx37)

write_csv(merged_data, "incoming_data/Spanish_Redux/SpanishMexicanWS_Marchman_Norming_data.csv", na = "")