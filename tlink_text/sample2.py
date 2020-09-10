import re

with open("00001-timex.txt",'r') as f:
   with open("1-timex.txt",'w')as f1:
       for line in f.readlines():
           line = str(line)
           print(line.replace('　\n','[\nJ\nS\nP\n]\n'))
           #print(re.sub(r'^\s*\n', '[\nJ\nS\nP\n]\n',line))
           cols = len(line[0].split("\t"))
           splitted = line.split("\t")
           #assert len(splitted) == 4
           f1.write("{}\n".format(splitted[0]))
       #print(re.sub(r'^[\\s|\u3000]+', '[\nJ\nS\nP]',line)
