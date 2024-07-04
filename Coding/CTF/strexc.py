import re
a=input()
b='7 5 4 6 4 6 4 3 2 3 9 9 4 3 6 7 5 3 12 8 5 5 4 9 3 8 3 4 2 2 3 9 3 6 3 5 6 2 8 3 6 4 1 6 5 5 6 8 10 3 3 6 3'
lst=re.split(r'\s+',b)
lst=[int(x) for x in lst]
#print(lst)
i=0
index=0
for i in range(len(lst)):
    index+=lst[i]
    a=a[:index]+","+a[index:]
    index+=1
print(a)
