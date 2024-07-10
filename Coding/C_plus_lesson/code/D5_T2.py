# 班级人数
n=int(input())
lst=[[0,0,0]for _ in range(n)]
lst_out=[]
cnt=0
for i in range(n):
    s = input()
    a,b,c=map(int,s.split())
    lst[cnt][0]=a
    lst[cnt][1]=b
    lst[cnt][2]=c
    if a>=90 and b>=90 and c>=90:
        lst_out.append(i)
if len(lst_out)>0:
    for k in range(len(lst_out)):
        print(lst_out[k])
else:
    print("None.")