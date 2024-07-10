import requests

# 发送GET请求
response = requests.get("https://example.com")

# 获取服务器返回的Cookie
cookies = response.cookies

# 打印Cookie
for cookie in cookies:
    print(f"Name: {cookie.name}, Value: {cookie.value}")