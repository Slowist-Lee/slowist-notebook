import requests  
url = 'https://slowist-lee.github.io/slowist-notebook/%E6%94%B6%E8%97%8F%E5%A4%B9/' # 生成get请求  
rqg = requests.get(url)  
# 查看结果类型  
print('查看结果类型：', type(rqg))  
# 查看状态码  
print('状态码：',rqg.status_code)  
# 查看编码  
print('编码 ：',rqg.encoding)  
# 查看响应头  
print('响应头：',rqg.headers)  
# 打印查看网页内容  
print('查看网页内容：',rqg.text)  
