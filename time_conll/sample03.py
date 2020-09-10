import re

text = ''
row = 'event_sent_id' + '\t' + 'event_index' + '\t' + 'event_word' + '\t' + 'event_id' + '\n'

with open("new_event_f.txt", 'r') as f:
    with open("new_event_f2.tsv", 'w')as f1:
        for line in f:
            words = re.split(r'\t|,|\n', line)

            if 'sent_id' in line:
                ln = line.replace("sent_id = ","")
                ln1 = ln.replace('\n','')
                #print(ln)

            else:
                row += '{}{}\t{}\t{}\n'.format(
                    ln1,
                    words[0],
                    words[1],
                    words[2]
                )

        print(row)
        f1.write(row)
            #lines = text
        #print(lines)
        # print(lines)
        #print(row)
        #f1.write(ln)
    f1.close()
f.close()
