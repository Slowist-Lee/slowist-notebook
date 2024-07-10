# import requests  
# import json
# headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","Accept": "application/json"} 
# # response = requests.get("https://www.baidu.com/",headers=headers)  
# # print(f"当前请求的响应状态码为：{response.status_code}")  
# # print(response.request.headers)
# # print(response.text)  
# # 在上面的基础上使用get和?来构造
# # 这是目标url  
# url = 'https://www.baidu.com/s?' 
# kw={'wd':'python',"pn":1}
# r = requests.get(url,headers=headers,params=kw)
# print(r.url) 
# http://eta.zju.edu.cn/


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置浏览器选项
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
url = 'http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
cookies = {"_ga=GA1.3.62059840.1695981862; lang=zh-CN; device_token=6a30766aabf43d7a7665e92f1ea7340c; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1717814709,1717916859,1717929942,1720249537; HMACCOUNT=259FB22B0B9404BD; JWTUser=%7B%22account%22%3A%223230103034%22%2C%22id%22%3A666992%2C%22tenant_id%22%3A112%7D; login_cmc_id=01fe548420d67e21806c3f12a7206247; login_cmc_tid=d66fa407c94328d37ce46c4b06efa9a3; group_code=1800000448; login_cmc_url=https%3A%2F%2Ftgmedia.cmc.zju.edu.cn%2Flogin1800000448.html; login_cmc_type=2; cmc_version=v3; _token=017aa45c248cab434338f3cc050523b681d3921b180d7b8e01e65fff23f21e1ba%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22_token%22%3Bi%3A1%3Bs%3A644%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMzIzMDEwMzAzNCIsImNtY0dyb3VwQ29kZSI6IjE4MDAwMDA0NDgiLCJjbWNHcm91cElkIjoiZjE4YjhmNGVlNDBiY2QwNzY1Y2ZlOTg3Y2E4MjA0NmUiLCJleHAiOjE3MjAzMzU5MzcsImxvZ2luVHlwZSI6ImRlZmF1bHQiLCJtcm9sZXMiOlt7ImNtY19yb2xlIjoiNmJiMmE0NWM3Yjc3NGJkNjZhZjMzYWRmODgwZmFlYTMiLCJjb2RlIjoic3R1ZGVudCIsImNyZWF0ZWRfYXQiOiIyMDIxLTA3LTMwIDE0OjQzOjE3IiwiZGVzY3JpcHRpb24iOiIiLCJkaXNwbGF5X25hbWUiOiLlrabnlJ8iLCJpZCI6MjA1LCJpc2RlZmF1bHQiOiIwIiwic3RhdHVzIjowfV0sInBhc3N3b3JkIjoiYjNmZTQ0NGY3ZWM4ZjE1MTA4NTI3YzMyNmVjNjIyMGIiLCJyZWFsbmFtZSI6IuadjuaYlSIsInN1YiI6NjY2OTkyLCJ0ZW5hbnRfaWQiOjExMn0.w_raRiyUKFjTLHzq0e8Kp3jIzYTnoXqK9ZgQRwy8eVk%22%3B%7D; Hm_lpvt_35da6f287722b1ee93d185de460f8ba2=1720249596; _csrf=S8mwplVi9KWoF2WQ0TlCeCWiecs7g0DhP83Tx0ZJ%2FhM%3D; _pv0=4doxtCkWSmPtZ8k4h59%2Btk05V01Yc2LYCfCuU2dkV9F9qKPmwchpDZHOWsV7w4dgMAedMauMNXmhr8iDKzQt%2Bv6SY8LgF1z662B6ARxWr3z6hf%2F36E%2F2ltAJUMqCiTBniRHzPIJB6p23E19DBUdoEdqtJU%2BsToYKb1xqLbD9IBKanYy8fZQokVUr1cRU6qaIJb9e%2F1OfQrz1%2F9i6Iru%2FOtufr3COw3EUPqckf5qTi4m%2BpOSDXlxX%2FdKrTiLELYO0EuwpC9ge5AT8LPtX5ne%2FF0%2FkM4JnNmFEpAlCBHdZJl72KDcSLt3F9PDNg19dd%2F62I9t7kky%2Fd4JGIePWvth%2BWj6hSYw2LJQMdgnt6i5p2tMzmFJa2H46LVfoOPKw%2FAPJ6scJgr57xhiuuJ%2BHthYnPCRad9P4%2F%2FSCp5SD1LmnFik%3D; _pf0=mz6SazkJNbcw2iwdpGXvl2oimzrhRV9fAvWOb9yMzfQ%3D; _pc0=3cvCeS6X4CFK0ff1i7Ylr2%2BWPU2lgi2s0VaD4pVxAtwwIR7keCdKX5T4oFyAjDiI; iPlanetDirectoryPro=dy2vevJMm908ONqo2y8v6WxnzLH5Gdb6TpVmMq8UgbxQsldMWgGJ%2FhbjpRG1C1iQof7MfWHd2XqQjAAsbDS5i5XvaAgUzo2nzBCoQrTGtCICeyjSG2yU7R8aAzF4%2FPdJfGAP1q%2BufBNHPPVvwOL5o4PTTQYeyHSPuoI%2F3eTbhrM4nb75AQ%2B5C13dIe%2Fdnp2WXwDjRfan0Hx0gVvvGRkyIPVDqt2idw5F1PNoXykymjhf6snYSuOWxRuTJmKYVbLoj967m%2Fv2NwPI1y3qdGgha%2B4pEJpd1PUvsh2OwCj1GxwSor%2FSG%2BoVbcPzvQJ1LrTF4iSWD9AHCAHuKjABSeyEkfgptaB5VzWJb%2FlD4RtG%2F1k%3D"}
# 添加Cookie到浏览器
for cookie in cookies:
    driver.add_cookie(cookie)

# 刷新页面以应用Cookie
driver.get('http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D')


# 关闭WebDriver
driver.quit()