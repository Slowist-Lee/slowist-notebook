from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# 设置ChromeDriver的路径
chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'  # 请将其替换为你的chromedriver路径

# 设置Chrome选项（例如无头模式）
chrome_options = Options()
# chrome_options.add_argument('--headless')  # 如果你不需要看到浏览器的界面，可以启用无头模式
chrome_options.add_argument('--disable-gpu')

# 创建ChromeDriver服务
service = Service(chromedriver_path)

# 启动Chrome浏览器
web = webdriver.Chrome(service=service, options=chrome_options)

# 打开网页
url = 'http://zdbk.zju.edu.cn/jwglxt/cxdy/xscjcx_cxXscjIndex.html?gnmkdm=N5083&layout=default&su=3230103034'  

web.get('http://zdbk.zju.edu.cn')

# 设置cookie
cookies=[
    {'domain': '.zju.edu.cn', 'httpOnly': False, 'name': 'iPlanetDirectoryPro', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8hr%2BT0wiWXeW0p6Jc0YVLGOjz13vnMU1Ta7dpFW8fzyo0L%2FmJlmODOr8uNy7v%2BzyOg%2B6bAveWeWHvuSdS6irdnqahEBMU4Y3kpAaTfttCn0FK%2FNau1Uh7ylSfujqGfJn21OQe1%2FIp04FT0fvAXlnpYL5K42pypwVHTXsPVRPdCMMO%2B5Y%2BthbCoDJwiEEDZazSZ2ggv7jtqYJk0%2FvZCRj%2FWXS1EP6OMpYynPfUMGFzsis9nepwoD%2FSOs8%2Bq2Qo6q8%2FxIIoyLz6H4uvI1037R93Yunt4LeEBivroLVQauvOJ9gPZH4%2BAaLySO%2Fd%2FkvoeMad4gws%2B82SQbpaA0FcSlUIpngYpa3ovTjpIEO1h8DEWk%3D'},
    {'domain': '.zju.edu.cn', 'httpOnly': True, 'name': '_pc0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '3cvCeS6X4CFK0ff1i7Ylr%2B0%2BpClSW37JIc9AL81K7%2FXzumpuOqzjIsRtNDuaHKb3'},
    {'domain': '.zju.edu.cn', 'expiry': 1720401195, 'httpOnly': True, 'name': '_pf0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'mz6SazkJNbcw2iwdpGXvlwRByUdxZXa6DfzQZM%2BCVmI%3D'},
    {'domain': '.zju.edu.cn', 'httpOnly': False, 'name': '_pv0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'T008vw87sSyD3i7TK%2B7U7ukJ2M5OO2E3spol225fKsGgsNmMKsFsljbvELIL3fy8BL1e%2B%2B22%2FmtH2m8CXp2hBji%2BJdLyuKStogFqIihzCS7kyPen6EGoRZuVUJ%2BgqvKZU5DnArQns9zW5bKc1vOnTof1E1BPzQ9l0snVfUsZkopgWaGCnLqQLI%2BRFqtCqalIVeQUrz0bM42GHcOx%2BQbPJyWZpdaA9bpsipA%2B4jzRfUlaHRJrcW%2F8fDQ3hqYygxfd8zJrlw%2B7TvGg3F5%2F9G1NJsM5UIplCOOhkSfEswJG8G7Pa%2FQ6kJ0zP1KpVPJ03pENgcIh4lBqFVzonjxfUEmrhRs3P1dDiyDyzOT83Xvpe8tkikmN4U6Y7XXcyk3MVNyL35IwYxXX1ISpCfre6Al0DZVe3JTQQ8xlS5bABCWbpRo%3D'},
    {'domain': '.zju.edu.cn', 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'S8mwplVi9KWoF2WQ0TlCeEhE9Ed3Z8AWoV1r0JO3Bh8%3D'},
    {'domain': 'zdbk.zju.edu.cn', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/jwglxt', 'sameSite': 'Lax', 'secure': False, 'value': 'BA10100052A2B825D2B7DF20E3D70631'},
    {'domain': 'zdbk.zju.edu.cn', 'httpOnly': False, 'name': 'route', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c2c4d5a14bbc5b6918b307746d272ddd'},
    {'domain': 'zdbk.zju.edu.cn', 'httpOnly': True, 'name': 'JSESSIONPREJSDM', 'path': '/jwglxt/xtgl', 'sameSite': 'Lax', 'secure': False, 'value': 'h%40Q%2CUB0Z%3AO%5EdJj%22%7BHZ4%5E0Q0B0DF3Z%3AO%5E'}
]

for cookie in cookies:
    web.add_cookie(cookie)


web.get(url)

# 刷新页面以使cookie生效
WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)
print(web.page_source)
# soup=BeautifulSoup(web,'lxml')
# value3=soup.find('input',id='4')['value']
# print(value3)
