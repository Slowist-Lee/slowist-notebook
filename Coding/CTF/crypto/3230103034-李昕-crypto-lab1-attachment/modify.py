text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

def mod_inverse(a, m):
    # Find the modular inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1  

def decrypt(s, k):
    out = ''
    for i in range(len(s)):
        index = text_list.index(s[i])  
        key_value = k[i % len(k)]
        if key_value == 0:
            key_value = 1  
        inverse_key = mod_inverse(key_value, 97)
        index *= inverse_key  
        index %= 97
        out += text_list[index] 
    return out


key = [0, 0, 0, 90, 67, 43, 0, 0, 0, 0, 0, 87, 76, 0, 0, 80, 13, 72, 0, 0, 92, 10, 0, 0, 0, 0, 0, 0, 0]

cipher = open('cipher.txt', 'r').read()  
plain = decrypt(cipher, key)
open('plain_decrypted.txt', 'w').write(plain)  