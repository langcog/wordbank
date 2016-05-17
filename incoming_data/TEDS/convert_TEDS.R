# DEMOGRAPHIC INFORMATION
# Id_twin (unique twin identifier)
# Id_fam (family identifier, unique to each twin pair)
# twin   (twin birth order, 1=elder 2=younger)
# Random  (permits selecting one twin at random from each pair, to give independence of data, coded 0/1)
# Aethnic (ethnic category: 1=white, 0=other)
# Sex1 (gender of twin: 0=female, 1=male)
# Zygos (twin pair zygosity, 1=MZ 2=DZ)
# Amohqual (maternal educational qualifications, 8-point ordinal scale)
# Ases  (composite social class based on parental education and occupation, standardised with mean 0.0 and SD 1.0)
# 
# AGE 2 MEASURES
# Brepage1  (age of twin on completion of parent-reported measures),
# converted to months and rounded down
# Bvc0011 to bvc1001  (100 item vocabulary checklist)
# Bvocab1 (vocabulary total on this scale)
# Bwu061  (does child combine words)
# Bs01s1 through bs12s1  (12 sentence complexity pairs)
# 
# AGE 3 MEASURES
# Crepage1 (age of twin on completion of parent-reported measures),
# converted to months and rounded down
# Cvc0001 (not yet talking)
# Cvc0011 to cvc1001  (100 item vocabulary checklist)
# Cvocab1   (vocabulary total on this scale)
# Cs00s1 (does child combine words)
# Cs01s1 through cs12s1) (12 sentence complexity pairs)
# 
# AGE 4 MEASURES
# Drepage1 (age of twin on completion of parent-reported measures),
# converted to months and rounded down
# Dvd011 through dvc481 (48 item vocabulary checklist)
# Dsay011  (overall evaluation of child’s language/sentences, 6 point scale)

library(dplyr)
library(haven)
library(readr)
library(foreign)
library(tidyr)

teds_raw <- read_spss("TEDS dataset for WordBank 110516.sav")

write_csv(teds_raw, "teds.csv")

# make long form
teds_long <- teds_raw %>% 
  gather(variable, value, btwoyear:dsay011) %>%
  separate(variable, into=c("age", "variable"), sep = 1) %>%
  mutate(age = ifelse(age == "b", 2, ifelse(age == "c", 3, 4))) %>%
  filter(!(variable %in% c("twoyear","threeyr","fouryr", "vocab1"))) %>%
  mutate(sex = ifelse(sex1 == 1, "male", "female"), 
         ethnicity = ifelse(aethnic == 1, "white", "other"),
         zygosity = ifelse(zygos == 1, "MZ","DZ"),
         ses = ases, 
         mom_ed = amohqual) %>%
  select(-sex1, -aethnic, -zygos, -ases, -amohqual)

# split out ages for later merging
ages <- filter(teds_long, variable == "repagem1") %>%
  rename(age_months = value) %>%
  select(id_twin, age, age_months)

# fours <- filter(d, variable != "repagem1", age == 4)

# take only the two- and three-year-olds
# drop NAs for age, as this is missing data
twos <- filter(teds_long, 
               age == 2, 
               variable != "repagem1") %>%
  spread(variable, value) %>%
  mutate(id_twin = factor(id_twin)) %>%
  left_join(ages %>% mutate(id_twin = factor(id_twin))) %>%
  filter(!is.na(age_months)) %>%
  select(-twin,-random, -age, -ses)

threes <- filter(teds_long, 
               age == 3, 
               variable != "repagem1") %>%
  spread(variable, value) %>%
  mutate(id_twin = factor(id_twin)) %>%
  left_join(ages %>% mutate(id_twin = factor(id_twin))) %>%
  filter(!is.na(age_months)) %>%
  select(-twin,-random, -age, -ses)

# Either a single excel file (by convention called WugeseWS_Dax, but doesn't have to be), with sheets named data, fields, and values;
# Or three csv files, with the names foo_data, foo_fields, and foo_values (where foo is WugeseWS_Dax by convention, but doesn't have to be).
# For the data sheet/file:
#   The first row should be column labels (whatever they might be in this dataset).
# Each other row should be a single CDI administration.

write_csv(twos, "../../raw_data/English_British_TEDS_2s/EnglishBritishTEDS2s_data.csv")
write_csv(threes, "../../raw_data/English_British_TEDS_3s/EnglishBritishTEDS3s_data.csv")

# The fields sheet/file is a mapping from the dataset's column labels to Wordbank's fields, and should have the following columns:
#   column: column labels from the data sheet/file (modulo case sensitivity) that will be extracted
# field: what Wordbank field to map the column label to
# MUST include study_id and at least one of data_age and (date_of_birth and date_of_test)
# can also optionally have any of birth_order, ethnicity, mom_ed, sex
# the rest (everything in group=item) MUST be in this dataset's instrument definition file's itemID column
# this is how the dataset's fields get mapped — it's tricky and important to get right
# group: whether this field should be associated with the administration, the child, or the data table for the instrument
# one of admin, child, or item
# type: how to treat the value(s) of this field
# study_id, study_momed: value as is
# birth_order, data_age: value is made into an integer
# date_of_birth, date_of_test: value is made into date
# ethnicity, sex, mom_ed, any type in group=item: value is mapped using value mapping

write_csv(data.frame(column = names(twos), 
           field = names(twos), 
           group = "item",
           type = "word"), 
          "../../raw_data/English_British_TEDS_2s/EnglishBritishTEDS2s_fields.csv")

write_csv(data.frame(column = names(threes), 
                     field = names(threes), 
                     group = "item",
                     type = "word"), 
          "../../raw_data/English_British_TEDS_3s/EnglishBritishTEDS3s_fields.csv")

# The values sheet/file is a mapping from the dataset's value to Wordbank's values, split by type, and should have the following columns:
#   type: one of the types in the field mapping sheet/file
# data_value: the value option in the dataset
# value: the short form (e.g. M) of the corresponding value option in Wordbank. The sets of value options in Wordbank are:
#   For ethnicity, defined in common/models.py
# (('A', 'Asian'), ('B', 'Black'), ('H', 'Hispanic'), ('W', 'White'), ('O', 'Other/Mixed'))
# For sex, defined in common/models.py
# (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
# For mom_ed, defined in common/management/commands/populate_momed.py
# {(1, 'None'), (2, 'Primary'), (3, 'Some Secondary'), (4, 'Secondary'), (5, 'Some College'), (6, 'College'), (7, 'Some Graduate'), (8, 'Graduate')}
# For all types in group=item, defined in e.g. instruments/schemas/Wugese_WS.py and equal to the choices for that type of item as given in the instrument definition file, e.g.
# [(u'understands', u'understands'), (u'produces', u'produces')]



