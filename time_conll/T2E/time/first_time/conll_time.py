import re

text = ''

with open("../../../merged/00054-ud.conll", 'r') as f:
    with open("./time_data/first_time_54.txt", 'w')as f1:
        for line in f:
            words = re.split(r'\t|,|\n', line)
            if '# text' in line:
                continue
            elif '# sent_id' in line:
                ln = line.replace("# ","")
                text += ln
            elif 'TIMEX' in line:
                id = words[0]
                word = words[1]
                time = words[10]
                tid1 = re.findall(r"t\d{1,5}", time)
                #print(tid1)
                tid2 = ''.join(tid1)
                 # print(tid2)
                text += id + '\t' + word + '\t' + tid2 + '\n'
            else:
                continue
            lines = text
        f1.write(lines)
f1.close()
