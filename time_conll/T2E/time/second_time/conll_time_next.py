import re

text = ''
row = 'time_sent_id' + '\t' + 'time_index' + '\t' + 'time_word' + '\t' + 'time_id' + '\n'

with open("../first_time/time_data/first_time_54.txt", 'r') as f:
    with open("./second_data/new_time_54.tsv", 'w')as f1:
        for line in f:
            words = re.split(r'\t|,|\n', line)

            if 'sent_id' in line:
                ln = line.replace("sent_id = ","")
                ln1 = ln.replace('\n','')
            else:
                row += '{}{}\t{}\t{}\n'.format(
                    ln1,
                    words[0],
                    words[1],
                    words[2]
                )
        #print(row)
        f1.write(row)
    f1.close()
f.close()
