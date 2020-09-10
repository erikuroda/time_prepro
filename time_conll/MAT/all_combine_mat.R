library(tidyverse)
lf = list.files(path = "./MAT/input", full.names = TRUE)
data = lapply(lf, read_tsv)
data_bind = do.call(bind_rows, data)
data_bind
write_tsv(data_bind, path = "./MAT/all_mat.tsv")