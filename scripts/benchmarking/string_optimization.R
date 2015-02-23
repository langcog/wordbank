strings = c("item_1", "item_2", "item_3", "item_4", "item_5",
            "item_6", "item_7", "item_8", "item_9", "item_10")

microbenchmark(str_replace(strings, "item_", ""),
               strsplit(strings, "item_"),
               strsplit(strings, "item_", fixed=TRUE),
               substr(strings, 6, nchar(strings)))