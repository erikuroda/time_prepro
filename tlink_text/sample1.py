f = open('event.txt','r')
lines = f.readlines()
for lines in lines:
    if 'reltype' in lines:
        print(lines)
