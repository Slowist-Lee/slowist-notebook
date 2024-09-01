from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import re
# 设置ChromeDriver的路径
chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'  # 请将其替换为你的chromedriver路径

# 设置Chrome选项（例如无头模式）
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--headless')  # 如果你不需要看到浏览器的界面，可以启用无头模式

# 创建ChromeDriver服务
service = Service(chromedriver_path)

# 启动Chrome浏览器
web = webdriver.Chrome(service=service, options=chrome_options)

# 打开教务网首页
web.get('https://www.cc98.org')

# 点击登录按钮
login_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/logOn']"))
)
login_button.click()
print("first finished")
# 等待身份认证页面加载
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.ID, 'loginName'))
)

# 输入用户名和密码
username_input = web.find_element(By.ID, 'loginName')
password_input = web.find_element(By.ID, 'loginPassword')
login_submit_button = web.find_element(By.CSS_SELECTOR, "button[type='submit']")


username_input.send_keys('Slowist')
password_input.send_keys('lx051607')
login_submit_button.click()

# 等待登录后的页面加载
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# 点击登录按钮
board_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/board/758']"))
)
board_button.click()

chatboard_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/topic/5930820']"))
)
chatboard_button.click()

floor_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/topic/5930820']"))
)
floor_button.click()
time.sleep(20)
web.quit()