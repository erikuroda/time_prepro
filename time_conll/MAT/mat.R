library(tidyverse)
dat1 = read_tsv("./MAT/correct/mat_54.tsv")
dat2 = read_tsv("./MAT/event1/second_event/second_data/second_event1_54.tsv")
dat3 = read_tsv("./MAT/event2/second_event/second_data/second_event2_54.tsv")
dat4 = read_tsv("./MAT/root1/second_root/second_data/second_root_54.tsv")
dat5 = read_tsv("./MAT/root2/second_root/second_data/second_root_54.tsv")
new_e1 = dat1 %>%
  inner_join(dat2, by = "event1_id")
new_e2 = new_e1 %>%
  inner_join(dat3, by = "event2_id") 
new_r = new_e2 %>% 
  inner_join(dat4, by = "event1_sent_id")
new_r2 = new_r %>%
  inner_join(dat5, by = "event2_sent_id") %>%
  select(
    event1_sent_id, event1_index, event1_word, event1_id, root1_index, root1_word, root1,
    event2_sent_id, event2_index, event2_word, event2_id, root2_index, root2_word, root2, reltype)
write_tsv(new_r2, path = "./MAT/input/new_mat_54.tsv")
