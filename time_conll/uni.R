library(tidyverse)

dat1 = read_tsv("new_t2e.tsv")
dat2 = read_tsv("new_time_f2.tsv")
dat3 = read_tsv("new_event_f2.tsv")

new_t = dat1 %>%
  inner_join(dat2, by = "time_id")

new_e = new_t %>%
  inner_join(dat3, by = "event_id") %>%
  select(
    time_sent_id, 
    time_index, 
    time_word, 
    time_id, 
    event_sent_id, 
    event_index, 
    event_word, 
    event_id, 
    reltype)

write_tsv(new_e, path = "new_e.tsv")




# write_tsv(new_e, path="new_e.tsv")