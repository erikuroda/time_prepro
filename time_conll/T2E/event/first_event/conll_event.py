import re

text = ''

with open("../../../merged/00054-ud.conll", 'r') as f:
    with open("./event_data/first_event_54.txt", 'w')as f1:
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
                eid1 = re.findall(r"e\d{1,5}",event)
                eid2 = eid1[0]
                text += id + '\t' + word + '\t' + eid2 + '\n'
            else:
                continue

            lines = text
        #print(lines)
            # print(lines)
        f1.write(lines)
f1.close()
