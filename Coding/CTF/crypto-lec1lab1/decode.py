text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

def mod_inverse(a, m):
    # Find the modular inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1  # If no modular inverse, return 1 (only for cases where a=0 in original key)

def decrypt(s, k):
    out = ''
    for i in range(len(s)):
        index = text_list.index(s[i])  # Encrypted index
        key_value = k[i % len(k)]
        if key_value == 0:
            key_value = 1  # Treat 0 as 1 because 0 has no inverse
        inverse_key = mod_inverse(key_value, 97)
        index *= inverse_key  # Decrypt index through multiplication with inverse
        index %= 97
        out += text_list[index]  # Abstract original string
    return out

# 已知的密钥
key = [0, 0, 0, 90, 67, 43, 0, 0, 0, 0, 0, 87, 76, 0, 0, 80, 13, 72, 0, 0, 92, 10, 0, 0, 0, 0, 0, 0, 0]

cipher = open('cipher.txt', 'r').read()  # 读取加密文本
plain = decrypt(cipher, key)
open('plain_decrypted.txt', 'w').write(plain)  # 将解密后的文本写入文件
