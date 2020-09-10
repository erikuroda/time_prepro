import re

text = ''

with open("00001-ud.conll", 'r') as f:
    with open("new_event_f.txt", 'w')as f1:
        for line in f:
            words = re.split(r'\t|,|\n', line)
            if '# text' in line:
                continue

            elif '# sent_id' in line:
                ln = line.replace("# ","")
                text += ln

            elif 'EVENT' in line:
                id = words[0]
                word = words[1]
                event = words[10]
                eid1 = re.findall(r"e\d{1,2}",event)
                eid2 = eid1[0]
                text += id + '\t' + word + '\t' + eid2 + '\n'

            #elif 'TIMEX' in line:
            #    id = words[0]
            #    word = words[1]
            #    time = words[10]
            #    tid1 = re.findall(r"t\d{1,2}", time)
            #    tid2 = tid1[0]
                 # print(tid2)
            #    text += id + '\t' + word + '\t' + tid2 + '\n'

            #if 'root' in line:
            #    id = words[0]
            #    word = words[1]
            #    # print('root')
            #    text += id + '\t' + word + '\t' + 'root' + '\n'

            else:
                continue

            lines = text
        print(lines)
            # print(lines)
        f1.write(lines)
f1.close()
