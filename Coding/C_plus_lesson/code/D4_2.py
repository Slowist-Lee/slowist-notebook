lst=input().split()
s="secret"
flag=True
last_index=0
while s in lst:
    flag= False
    secret_index=lst.index(s)
    print(f"\"secret\" is pos {last_index+secret_index+1}")
    last_index+=(secret_index+1)
    lst=lst[secret_index+1:]
if flag:
    print("No \"secret\"")