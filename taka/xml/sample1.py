f = open('event.txt','r')
f1 = open('event2.txt','w')
lines = f.readlines()
for lines in lines:
    if 'reltype' in lines:
            #print(lines)
        f1.write(lines)
