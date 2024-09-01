import math
f=open("cipher.txt",encoding='utf-8')
content=f.read()
f.close()
s=[]
for i in range(len(content)):
    if content[i:i+3]=='{gY':
        s.append(i)
dif=[]
for i in range(len(s)-1):
    dif.append(s[i+1]-s[i])
gcd=dif[0]
for i in range(1,len(dif)):
    gcd=math.gcd(gcd,dif[i])
print(gcd)