from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 替换为你的ChromeDriver路径
chrome_driver_path = 'path/to/chromedriver'

# 设置Chrome选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # 最大化窗口

# 初始化WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开目标网站
driver.get('http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D')

# 等待用户手动登录
print("请手动登录...")
while not driver.current_url.startswith("https://example.com/dashboard"):  # 替换为登录后重定向的URL前缀
    time.sleep(5)

# 登录成功后获取cookies
cookies = driver.get_cookies()
print("登录成功，获取到的cookies如下：")
for cookie in cookies:
    print(cookie)

# 关闭浏览器
driver.quit()
