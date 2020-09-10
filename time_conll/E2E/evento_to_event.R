library(tidyverse)

dat1 = read_tsv("./E2E/correct/e2e_54.tsv")
dat2 = read_tsv("./E2E/event1/second_event/second_data/second_event1_54.tsv")
dat3 = read_tsv("./E2E/event2/second_event/second_data/second_event2_54.tsv")

new_t = dat1 %>%
  inner_join(dat2, by = "event1_id")

new_e = new_t %>%
  inner_join(dat3, by = "event2_id") %>%
  select(
    event1_sent_id, event1_index, event1_word, event1_id, 
    event2_sent_id, event2_index, event2_word, event2_id, 
    reltype)

write_tsv(new_e, path = "./E2E/input/new_e2e_54.tsv")
