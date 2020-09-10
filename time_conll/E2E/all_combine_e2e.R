library(tidyverse)
lf = list.files(path = "./E2E/input", full.names = TRUE)
data = lapply(lf, read_tsv)
data_bind = do.call(bind_rows, data)
data_bind
write_tsv(data_bind, path = "./E2E/all_e2e.tsv")