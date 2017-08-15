inst_dirs <- list.dirs("~/projects/lab/wordbank-site/raw_data",
                     recursive = FALSE)

dup_cols <- map_df(inst_dirs, function(inst_dir) {
  field_files <- list.files(inst_dir, "*_fields.csv", full.names = TRUE)
  map_df(field_files, function(field_file) {
    print(field_file)
    fields <- read_csv(field_file)
    fields %>%
      group_by(group, column) %>%
      filter(n() > 1, !is.na(column)) %>%
      mutate(inst = basename(field_file))
  })
})

datasets <- jsonlite::read_json("~/projects/lab/wordbank-site/static/json/datasets.json")

missing_cols <- map_df(inst_dirs, function(inst_dir) {
  data_files <- list.files(inst_dir, "*_data.csv", full.names = TRUE)
  field_files <- list.files(inst_dir, "*_fields.csv", full.names = TRUE)
  map2_df(data_files, field_files, function(data_file, field_file) {
    print(field_file)
    data <- read_csv(data_file, n_max = 1)
    fields <- read_csv(field_file)
    dataset <- datasets %>%
      keep(~basename(.x$file) == sub("(.*)_data.csv", "\\1.csv",
                                     basename(data_file))) %>%
      unlist()
    if (as.logical(dataset["splitcol"])) {
      item_cols <- fields %>% filter(type == "word", !is.na(column)) %$%
        column %>% tolower()
      cols <- c(paste(item_cols, "u", sep = ""),
                paste(item_cols, "p", sep = ""),
                tolower(filter(fields, type != "word", !is.na(column))$column))
    } else {
      cols <- fields %>% filter(!is.na(column)) %$% column %>% tolower()
    }
    data_frame(missing = setdiff(cols, tolower(names(data)))) %>%
      mutate(inst = basename(field_file))
  })
})
