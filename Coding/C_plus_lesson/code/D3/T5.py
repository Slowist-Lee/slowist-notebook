import re
n=int(input())
id1=['' for j in range(n)]
age=[0 for k in range(n)]

#感觉比如字典这样的结构可能更方便一点，但是排序就未知了qwq

for i in range(n):
    s1=re.split(r'\s',input())
    id1[i]=s1[0]
    age[i]=s1[1] #同理，多写了一行，有代码冗余问题
#print(id)
#print(age)
for i in range(n):
    k=i
    for j in range(i+1,n):
        if age[j]>age[k]:
            k=j
    id1[k],id1[i]=id1[i],id1[k]
    age[k],age[i]=age[i],age[k]
for i in range(n):
    print(id1[i])
#    print(age[i])