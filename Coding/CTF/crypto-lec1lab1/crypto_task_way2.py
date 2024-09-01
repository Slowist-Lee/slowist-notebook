import math
from collections import Counter

# 已知的字符列表
text_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

# 读取密文内容
with open("cipher.txt", encoding='utf-8') as f:
    content = f.read()

# 统计字符'e'的出现位置
char_to_find = 'e'
char_positions = [i for i, char in enumerate(content) if char == char_to_find]

# 检查字符之间的距离以计算最大公约数
if len(char_positions) < 2:
    raise ValueError("字符'e'出现次数不足以计算最大公约数")

differences = [char_positions[i + 1] - char_positions[i] for i in range(len(char_positions) - 1)]
gcd = differences[0]
for diff in differences[1:]:
    gcd = math.gcd(gcd, diff)

# # 确定密钥长度
key_length = 29  # 根据上一步得出
# if gcd % key_length != 0:
#     raise ValueError("无法确定字符'e'的密钥，可能的密钥长度不正确")

# 确定字符'e'的加密密钥值
encrypted_positions = [text_list.index(content[pos]) for pos in char_positions]
original_position = text_list.index(char_to_find)

keys = []
for enc_pos in encrypted_positions:
    if original_position != 0:
        key = (enc_pos * pow(original_position, -1, 97)) % 97
        keys.append(key)
    else:
        keys.append(0)

# 取最常见的密钥作为推断结果
most_common_key = Counter(keys).most_common(1)[0][0]
print(f"字符'e'的推测密钥值: {most_common_key}")

# 将推断结果插入密钥列表中
keylst = [0 for _ in range(key_length)]
for pos in char_positions:
    keylst[pos % key_length] = most_common_key

print("推断出的密钥列表:", keylst)
