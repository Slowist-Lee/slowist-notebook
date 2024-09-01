# in a mess qwq 
# just because i didn't solve it so tried a lot of ways

import math
text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
f=open("cipher.txt",encoding='utf-8')
content=f.read()
f.close()
s_count=[]
s_all=[]
idx=[]
k=0
def bubble_sort_descending(arr,lst,idx):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                lst[j], lst[j+1] = lst[j+1], lst[j]
                idx[j], idx[j+1] = idx[j+1], idx[j]
for i in range(len(content)):
    if content[i:i+3] not in s_all:
        s_all.append(content[i:i+3])
        s_count.append(1)
        idx.append(i)
    else:
        s_count[s_all.index(content[i:i+3])]+=1
bubble_sort_descending(s_count,s_all,idx)
print(s_all[:10])
print(s_count[:10])
lst_the=s_all[:10]
keylst=[0 for _ in range(29)]
for m in lst_the:
    if m==' {g' or m =="gY ":
        continue
    print(m)
    print((idx[s_all.index(m)])%29)
    s=[]
    for i in range(len(content)):
        if content[i:i+3]== m:
            s.append(i)
    dif=[]
    for i in range(len(s)-1):
        dif.append(s[i+1]-s[i])
    gcd=dif[0]
    for i in range(1,len(dif)):
        gcd=math.gcd(gcd,dif[i])
    if gcd%29!=0:
        break
    maybe_the= m 
    out=[text_list.index(i) for i in maybe_the] #encrypted data
    index=[text_list.index(i) for i in 'the'] #original data
    # key = [(out[i]*pow(index[i],-1,97))%97 for i in range(3)]
    key = [(out[i]*pow(index[i],-1,97))%97 if out[i] != 0 and index[i] != 0 else 0 for i in range(3)]

    print(out,index)
    print(key)
    for i in range(3):
        keylst[(idx[s_all.index(m)])%29+i]=key[i]
print(keylst)

s=[]
for i in range(len(content)):
    if content[i:i+3]==' X&':
        s.append(i)
dif=[]
for i in range(len(s)-1):
    dif.append(s[i+1]-s[i])
gcd=dif[0]
for i in range(1,len(dif)):
    gcd=math.gcd(gcd,dif[i])
print(gcd)

maybe_the='{gY'
out=[text_list.index(i) for i in maybe_the] #encrypted data
index=[text_list.index(i) for i in 'the'] #original data
key = [(out[i]*pow(index[i],-1,97))%97 for i in range(3)]
print(out,index)
print(key)

maybe_the=' X&'

out=[text_list.index(i) for i in maybe_the] #encrypted data
index=[text_list.index(i) for i in 'the'] #original data
key = [(out[i]*pow(index[i],-1,97))%97 for i in range(3)]
print(out,index)
print(key)

# these are known keys
# then abstract the first 29 letters and count the letters

# print(content[30:60])

s2=" ur {gY ),yPT	Yb;85SY8 o:|k'y^"
s2=' %n` f@XP b	zbJY?] 8Q" [CP	|;o'
s2lst=[]
for j in s2:
    s2lst.append(j)
print(s2lst)
slst=[]
for i in range(len(s2lst)):
    if s2lst[i] not in slst:
        slst.append(s2lst[i])
    s2lst[i]=chr(65+slst.index(s2lst[i]))
ans=''.join(s2lst)
print(ans)

s2=" ur {gY ),yPT	Yb;85SY8 o:|k'y^"
s2=' %n` f@XP b	zbJY?] 8Q" [CP	|;o'
s2lst=[]
for j in s2:
    s2lst.append(j)
print(s2lst)
slst=[]
for i in range(len(s2lst)):
    if s2lst[i] not in slst:
        slst.append(s2lst[i])
    s2lst[i]=chr(65+slst.index(s2lst[i]))
ans=''.join(s2lst)
print(ans)


