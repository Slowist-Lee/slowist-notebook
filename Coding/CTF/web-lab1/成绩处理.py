from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# 设置ChromeDriver的路径
chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'

# 设置Chrome选项（例如无头模式）
chrome_options = Options()
# chrome_options.add_argument('--headless')  # 如果你不需要看到浏览器的界面，可以启用无头模式
chrome_options.add_argument('--disable-gpu')

# 创建ChromeDriver服务
service = Service(chromedriver_path)

# 启动Chrome浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开网页
url = "http://zdbk.zju.edu.cn/jwglxt/xtgl/login_slogin.html"
driver.get(url)

# 显式等待，直到按钮出现
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, 'ssodl')))
    
# 点击按钮
button.click()

# 等待页面跳转（确保等待足够时间让新页面加载）
wait.until(EC.url_changes(url))

# 更新当前页面的URL
new_url = driver.current_url
username_input = wait.until(EC.visibility_of_element_located((By.XPATH, 'username')))
username_input.send_keys('3230103034')

 
# 显式等待，直到密码输入框出现
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, 'password')))
# 输入密码并按下回车键
password_input.send_keys('lx051607', Keys.ENTER)
wait.until(EC.url_changes(new_url))

# # 等待一些时间以查看效果（仅用于调试，可以根据需要调整或删除）
# WebDriverWait(driver, 10).until(EC.url_changes(url))