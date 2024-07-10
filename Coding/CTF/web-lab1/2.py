import requests  
url= "https://slowist-lee.github.io/zjuers-slowist-version/"
r = requests.get(url)
print(r.text)  