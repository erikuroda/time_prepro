import re

text = ''
row = 'event2_sent_id' + '\t' + 'root_index' + '\t' + 'root_word' + '\t' + 'root' + '\n'

with open("../first_root/first_data/first_root_54.txt", 'r') as f:
    with open("./second_data/second_root_54.tsv", 'w')as f1:
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
        f1.write(row)
    f1.close()
f.close()
