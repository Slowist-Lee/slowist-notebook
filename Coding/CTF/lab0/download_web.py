import requests

url = 'http://pumpk1n.com/lab0.php'  
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    webpage_content = response.text

    # 将网页内容保存到文件中
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(webpage_content)
    
    print("Webpage downloaded and saved successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
