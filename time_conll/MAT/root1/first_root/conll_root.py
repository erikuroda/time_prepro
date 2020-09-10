import re

text = ''

with open("../../../merged/00054-ud.conll", 'r') as f:
    with open("./first_data/first_root_54.txt", 'w')as f1:
        for line in f:
            words = re.split(r'\t|,|\n', line)
            if '# text' in line:
                continue
            elif '# sent_id' in line:
                ln = line.replace("# ","")
                text += ln
            elif 'root' in line:
                id = words[0]
                word = words[1]
                text += id + '\t' + word + '\t' + 'root' + '\n'
            else:
                continue
            lines = text
        f1.write(lines)
f1.close()
