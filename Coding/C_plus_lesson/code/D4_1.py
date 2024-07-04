def LstSort(lst,lenlst):
    for i in range(0,lenlst):
        k=i
        for j in range(i+1,lenlst):
            if lst[j][1]>lst[k][1] or (lst[j][1]==lst[k][1] and lst[j][0]<lst[k][0]):
                k=j
        if k!=i:
            lst[i],lst[k]=lst[k],lst[i]
def PrintLst(lst,lenlst):
    for i in range(0,lenlst):
        print(i+1,lst[i][0],lst[i][1])

n,m = map(int, input().split())
n=int(n);m=int(m)
flst=[['',0] for _ in range(n)]
mlst=[['',0] for _ in range(m)]
for i in range(n):
    name,vote=input().split()
    flst[i][0]=name
    flst[i][1]=int(vote)
s=input()
for j in range(m):
    name,vote=input().split()
    mlst[j][0]=name
    mlst[j][1]=int(vote)
s=input()
inputstring=input()
while inputstring!="END":
    if inputstring=='PK FEMALE':
        print(inputstring)
        LstSort(flst,n)
        PrintLst(flst,n)
    elif inputstring=='PK MALE':
        print(inputstring)
        LstSort(mlst,m)
        PrintLst(mlst,m)
    else:
        vote_str=inputstring[5:]
        i,j=map(int, vote_str.split())
        if 1<=i<n+1 and 1<=j<m+1:
            flst[i-1][1]+=1
            mlst[j-1][1]+=1
    inputstring=input()
lst=flst+mlst
print('END')
LstSort(lst,m+n)
PrintLst(lst,m+n)