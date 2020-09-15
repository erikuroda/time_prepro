readStream1 = open("dct.txt", "r");
context1 = readStream1.read();
a = context1.split('\n') # 从文档 list.txt 取得的关键词数组
size = len(a)
b = [ 0 ]*size # 对应关键字数组 a，创建一个整型数组 b，每个元素的初始值为零。
result = open("new.txt","w")
fo = open("event2.txt", "r")
try:
 while True:
     line = fo.readline()
     if line:
          index= 0
          for v in a:
              if line.find(" " + v) > -1:
                  v = v + "  " + line
                  b[index] = b[index] + 1
                  result.write(v)
              index = index + 1
     else:
         break
finally:
   fo.close()
