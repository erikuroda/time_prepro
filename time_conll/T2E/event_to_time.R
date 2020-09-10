library(tidyverse)

dat1 = read_tsv("./T2E/correct/t2e_54.tsv")
dat2 = read_tsv("./T2E/time/second_time/second_data/new_time_54.tsv")
dat3 = read_tsv("./T2E/event/second_event/second_data/second_event_54.tsv")

new_t = dat1 %>%
  inner_join(dat2, by = "time_id")

new_e = new_t %>%
  inner_join(dat3, by = "event_id") %>%
  select(
    time_sent_id, time_index, time_word, time_id, 
    event_sent_id, event_index, event_word, event_id, 
    reltype)

write_tsv(new_e, path = "./T2E/input/new_t2e_54.tsv")

