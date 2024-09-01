import requests
import re
sess=requests.Session()
url = 'http://pumpk1n.com/lab0.php'  
response = sess.get(url)


# 第一次循环

if response.status_code == 200:
    content = response.text 
# print(response.text)
    r = re.findall(r"token=(.*)'",content)
    token=r[0]

# 剩下1336次

for i in range(1337):
    response = sess.get(f'http://pumpk1n.com/lab0.php?token={token}')
    if response.status_code == 200:
        content = response.text 
        # print(response.text)
        r = re.findall(r"token=(.*)'",content)
        token=r[0]
    response=sess.get(url=f'http://www.pumpk1n.com/flag.php?token={token}')

# 最后一次之后，得到flag
content = response.text
print(content)



