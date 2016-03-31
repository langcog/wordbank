library(readxl)
library(purrr)

bsl <- read_excel("../raw_data/BSL_WG/deafCDI_clex.xlsx")
names_bsl <- names(bsl) %>%
  map_chr(function(s) {
    last <- substr(s, nchar(s), nchar(s))
    if (last == "1") {
      return(paste0(substr(s, 1, nchar(s) - 1), "u"))
    } else if (last == "2") {
      return(paste0(substr(s, 1, nchar(s) - 1), "p"))
    } else {
      return(s)
    }
  })

names(bsl) <- names_bsl
write.csv(bsl, "../raw_data/BSL_WG/BSLWG_Woll_data.csv", row.names = FALSE)
