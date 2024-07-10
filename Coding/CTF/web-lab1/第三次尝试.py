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
web.get('http://zdbk.zju.edu.cn')

# 点击登录按钮
login_button = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.ID, 'ssodl'))
)
login_button.click()
print("first finished")
# 等待身份认证页面加载
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.ID, 'username'))
)

# 输入用户名和密码
username_input = web.find_element(By.ID, 'username')
password_input = web.find_element(By.ID, 'password')
login_submit_button = web.find_element(By.ID, 'dl')

username_input.send_keys('3230103459')
password_input.send_keys('02371190lt')
login_submit_button.click()

# 等待登录后的页面加载
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# 打开目标页面
url = 'http://zdbk.zju.edu.cn/jwglxt/cxdy/xscjcx_cxXscjIndex.html?gnmkdm=N5083&layout=default&su=3230103034'
web.get(url)
time.sleep(20)
# 等待目标页面加载
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)


web.execute_script("document.getElementById('xn_cx').value = '2023-2024';")

web.execute_script("document.getElementById('xq_cx').value = '1';")

submit_button = web.find_element(By.ID, 'search_go')
submit_button.click()
time.sleep(10)

pattern = re.compile(r'<td[^>]*?title="([^"]*?)"[^>]*?aria-describedby="tabGrid_kcmc">[^<]*?</td><td[^>]*?title="(\d+)"[^>]*?aria-describedby="tabGrid_cj">[^<]*?</td><td[^>]*?title="\d+(\.\d+)?[^>]*?aria-describedby="tabGrid_xf">[^<]*?</td><td[^>]*?title="(\d+(\.\d+)?)"[^>]*?aria-describedby="tabGrid_jd">[^<]*?</td>')

matches = pattern.findall(web.page_source)
lstkj=['94','91','88','85','82','79','76','73','70','67','64','61']
lstbl=['95','92','89','86','83','80','77','74','71','68','65','62']
kj=0
bl=0
# 打印匹配结果
print("2023-2024 Autumn-Winter")
for match in matches:
    course_name = match[0]
    grade = match[1]
    gpa = match[3]
    if grade in lstkj:
        kj+=1
    if grade in lstbl:
        bl+=1
    print(f"course_name: {course_name}, grade: {grade}, GPA: {gpa}")
print("你这学期一共卡绩",kj,"门")
print("你这学期一共被捞",bl,"门")
print("-------------------")
print("2023-2024 Spring-Summer")
web.execute_script("document.getElementById('xn_cx').value = '2023-2024';")
web.execute_script("document.getElementById('xq_cx').value = '2';")
submit_button = web.find_element(By.ID, 'search_go')
submit_button.click()
time.sleep(10)
# 正则表达式匹配课程名称和成绩
pattern = re.compile(r'<td[^>]*?title="([^"]*?)"[^>]*?aria-describedby="tabGrid_kcmc">[^<]*?</td><td[^>]*?title="(\d+)"[^>]*?aria-describedby="tabGrid_cj">[^<]*?</td><td[^>]*?title="\d+(\.\d+)?[^>]*?aria-describedby="tabGrid_xf">[^<]*?</td><td[^>]*?title="(\d+(\.\d+)?)"[^>]*?aria-describedby="tabGrid_jd">[^<]*?</td>')
matches = pattern.findall(web.page_source)
kj=0
bl=0
for match in matches:
    course_name = match[0]
    grade = match[1]
    gpa = match[3]
    if grade in lstkj:
        kj+=1
    if grade in lstbl:
        bl+=1
    print(f"course_name: {course_name}, grade: {grade}, GPA: {gpa}")
print("你这学期一共卡绩",kj,"门")
print("你这学期一共被捞",bl,"门")

web.quit()