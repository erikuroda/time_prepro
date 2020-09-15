f = open('n1.txt','r')
f1 = open('n2.txt','w')
lines = f.readlines()
for lines in lines:
    if 'reltype' in lines:
            #print(lines)
        f1.write(lines)
