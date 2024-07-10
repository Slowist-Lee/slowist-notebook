from selenium import webdriver
import time
import requests
import json
browser = webdriver.Chrome()
url = "http://eta.zju.edu.cn/" 
browser.get(url)
time.sleep(20)
cookies = browser.get_cookies()
# print("Cookies:", cookies)
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
# print("cookies_dict", cookies_dict)
browser.execute_script("window.open()")

# 获取页面内容
time.sleep(5)
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "JSESSIONID=6C0DC410E28C9AC2577739EC9FC0C66C; _ga=GA1.3.62059840.1695981862; lang=zh-CN; device_token=6a30766aabf43d7a7665e92f1ea7340c; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1717318403,1717814709,1717916859,1717929942; _csrf=S8mwplVi9KWoF2WQ0TlCeIMI4HWZh2SENr75QbFMz2g%3D; _pv0=PuNv7E7%2FOjxqL3Y4M61HXrBRLpMq1Zp2eflnfQ%2FaITCkDoF19FXhEL7dlwN7vrezP8%2BuIycJa4FOoo2%2Fg6CtA818NBLgHs3fFMQjoPgpE%2BKtZ9AAh0D1DxBahzVd%2FF1u4clnwn9Y1gAW3mgAiApfJuUt%2F9K4siey%2FcsvAiiLYxPDogMxTXys71XjboDJ9a27BpuHfp9qjBOg%2Bt0k%2FZ9q7QCWvv68kJBxXz3Unk%2FiOMgstRJoacH93O5DFFM16RZUkbxJeIFzUdvPkjEgxBfaC0Qq5NDPnDN2zAdf2rF8A866lhsR6gpPlkyCcfCNC0UM0DyfzPiNa9KLus0INdiqPs3kdxgmT6CJSnHlgMTnDiOG9VIRReTKRU2E8byHWzKKb3v63T9DHJpbq9WhifdLnB4DVsutAAPM6c9Rwxv5sV8%3D; _pf0=mz6SazkJNbcw2iwdpGXvl1qv5zcVOPLXceApZqhPa3A%3D; _pc0=3cvCeS6X4CFK0ff1i7Ylr2vdo6ce5XKR0JMadWI%2FynADqHfC7fBD%2F6YAjpVpper6; iPlanetDirectoryPro=KtUv6b1SpCAWrZgGu1gXW31RNdzVH9QdcBI%2Bhql1fubLK531X3VyV5o%2B%2BsZSxjUuJvper30MOvk6DxfdO2HFtUisRyb6gZS3KNi0FbHK2tGZ6MIqNzSD3FjSGbJxHvbuIbXiPY%2F54gmlvN23Ot70%2FWqT%2BYKrcSFYk5Ar4Ghf0bHspwGAb5gPTA8z9ke1tdUqtqjwb117kXsldn1%2B83xY8Xfg3I29tZrNTNAlW0WY1jSwGBWXyCvofFCLMUeCeP%2BV7VH2U1DmPnRf68ZFuUQjgkGbwWr%2BZOh6JT51wYkdfvdhFqRO43KGxf192KPeOmzJomBOBcIuFj%2F%2BNScdbaWB8mvNOGPW%2BFSSufPjRN2i438%3D",
    "Host": "eta.zju.edu.cn",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


url="http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D"
response = requests.get(url, headers=headers, cookies=cookies_dict)

from bs4 import BeautifulSoup

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "JSESSIONID=6C0DC410E28C9AC2577739EC9FC0C66C; _ga=GA1.3.62059840.1695981862; lang=zh-CN; device_token=6a30766aabf43d7a7665e92f1ea7340c; Hm_lvt_35da6f287722b1ee93d185de460f8ba2=1717318403,1717814709,1717916859,1717929942; _csrf=S8mwplVi9KWoF2WQ0TlCeIMI4HWZh2SENr75QbFMz2g%3D; _pv0=PuNv7E7%2FOjxqL3Y4M61HXrBRLpMq1Zp2eflnfQ%2FaITCkDoF19FXhEL7dlwN7vrezP8%2BuIycJa4FOoo2%2Fg6CtA818NBLgHs3fFMQjoPgpE%2BKtZ9AAh0D1DxBahzVd%2FF1u4clnwn9Y1gAW3mgAiApfJuUt%2F9K4siey%2FcsvAiiLYxPDogMxTXys71XjboDJ9a27BpuHfp9qjBOg%2Bt0k%2FZ9q7QCWvv68kJBxXz3Unk%2FiOMgstRJoacH93O5DFFM16RZUkbxJeIFzUdvPkjEgxBfaC0Qq5NDPnDN2zAdf2rF8A866lhsR6gpPlkyCcfCNC0UM0DyfzPiNa9KLus0INdiqPs3kdxgmT6CJSnHlgMTnDiOG9VIRReTKRU2E8byHWzKKb3v63T9DHJpbq9WhifdLnB4DVsutAAPM6c9Rwxv5sV8%3D; _pf0=mz6SazkJNbcw2iwdpGXvl1qv5zcVOPLXceApZqhPa3A%3D; _pc0=3cvCeS6X4CFK0ff1i7Ylr2vdo6ce5XKR0JMadWI%2FynADqHfC7fBD%2F6YAjpVpper6; iPlanetDirectoryPro=KtUv6b1SpCAWrZgGu1gXW31RNdzVH9QdcBI%2Bhql1fubLK531X3VyV5o%2B%2BsZSxjUuJvper30MOvk6DxfdO2HFtUisRyb6gZS3KNi0FbHK2tGZ6MIqNzSD3FjSGbJxHvbuIbXiPY%2F54gmlvN23Ot70%2FWqT%2BYKrcSFYk5Ar4Ghf0bHspwGAb5gPTA8z9ke1tdUqtqjwb117kXsldn1%2B83xY8Xfg3I29tZrNTNAlW0WY1jSwGBWXyCvofFCLMUeCeP%2BV7VH2U1DmPnRf68ZFuUQjgkGbwWr%2BZOh6JT51wYkdfvdhFqRO43KGxf192KPeOmzJomBOBcIuFj%2F%2BNScdbaWB8mvNOGPW%2BFSSufPjRN2i438%3D",
    "Host": "eta.zju.edu.cn",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://eta.zju.edu.cn/index/xycj?xh=tRgSKjyqlp2a4mnK7DLtKw%253D%253D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}


# 检查响应状态码
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 例如，获取所有表格中的数据
    if data.get("code") == 0:
    items = data.get("data", {}).get("items", [])
            for item in items:
                # 提取成绩信息
                学年 = item.get("XN")
                成绩 = item.get("CJ")
                学期 = item.get("XQ")
                绩点 = item.get("JD")
                课程名称 = item.get("KCMC")
                学分 = item.get("XF")
                
                # 打印成绩信息
                print(f"学年: {学年}, 成绩: {成绩}, 学期: {学期}, 绩点: {绩点}, 课程名称: {课程名称}, 学分: {学分}")
    # tables = soup.find_all('table')
    # for table in tables:
    #     rows = table.find_all('tr')
    #     for row in rows:
    #         cols = row.find_all('td')
    #         cols = [col.get_text(strip=True) for col in cols]
    #         print(cols)
else:
    print("请求失败，状态码:", response.status_code)
    print("响应文本:", response.text)

# data = response.json()
# if response.status_code == 200:
#     try:
#         data = response.json()
#         if data.get("code") == 0:
#             items = data.get("data", {}).get("items", [])
#             for item in items:
#                 # 提取成绩信息
#                 学年 = item.get("XN")
#                 成绩 = item.get("CJ")
#                 学期 = item.get("XQ")
#                 绩点 = item.get("JD")
#                 课程名称 = item.get("KCMC")
#                 学分 = item.get("XF")
                
#                 # 打印成绩信息
#                 print(f"学年: {学年}, 成绩: {成绩}, 学期: {学期}, 绩点: {绩点}, 课程名称: {课程名称}, 学分: {学分}")
#         else:
#             print("请求失败或返回数据异常")
#     except json.JSONDecodeError:
#         print("响应内容不是有效的JSON：", response.text)
# else:
#     print("请求失败，状态码:", response.status_code)
#     print("响应文本:", response.text)

# 关闭浏览器
browser.quit()

# # 检查响应是否成功
# if data.get("code") == 0:
#     items = data.get("data", {}).get("items", [])
#     for item in items:
#         # 提取成绩信息
#         学年 = item.get("XN")
#         成绩 = item.get("CJ")
#         学期 = item.get("XQ")
#         绩点 = item.get("JD")
#         课程名称 = item.get("KCMC")
#         学分 = item.get("XF")
        
#         # 打印成绩信息
#         print(f"学年: {学年}, 成绩: {成绩}, 学期: {学期}, 绩点: {绩点}, 课程名称: {课程名称}, 学分: {学分}")
# else:
#     print("请求失败或返回数据异常")
# # 关闭浏览器
# browser.quit()

