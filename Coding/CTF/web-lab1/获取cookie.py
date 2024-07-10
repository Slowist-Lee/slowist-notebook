from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 启动Chrome浏览器
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # 请将'path/to/chromedriver'替换为您的chromedriver路径
driver = webdriver.Chrome(service=service)

# 打开目标网页
driver.get('http://zdbk.zju.edu.cn/jwglxt/cxdy/xscjcx_cxXscjIndex.html?gnmkdm=N5083&layout=default&su=3230103034')  # 请将'https://example.com/login'替换为您的目标登录页面URL

# 在这里手动登录
print("请手动登录并按回车键继续...")
input()

# 获取当前页面的所有cookie
cookies = driver.get_cookies()

# 打印所有cookie
for cookie in cookies:
    print(cookie)

# 关闭浏览器
driver.quit()
