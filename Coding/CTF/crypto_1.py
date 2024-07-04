from PIL import Image

width = 64  # 符号的宽度
height = 64  # 符号的高度
str1 = ""

def bw_judge(R, G, B):
    Gray_scale = 0.299 * R + 0.587 * G + 0.114 * B
    return Gray_scale < 128  # 调整阈值

def symbol_hash(symbol):
    return hash(tuple(tuple(row) for row in symbol))

image = Image.open("D:/My Repository/slowist-notebook/docs/Coding/CTF/crypto_challenge1.png")
pixels = image.load()
symbolpool = []
symbolcnt = []

for row in range(13):
    for col in range(21):
        symbol = [[0 for _ in range(height)] for _ in range(width)]  # 一个存放符号的矩阵
        for i in range(64):
            for j in range(64):
                R, G, B = pixels[j + 64 * col, i + 64 * row]
                symbol[i][j] = int(bw_judge(R, G, B))

        symbol_hash_value = symbol_hash(symbol)
        if symbol_hash_value in symbolpool:
            idx = symbolpool.index(symbol_hash_value)
            symbolcnt[idx] += 1
        else:
            symbolpool.append(symbol_hash_value)
            symbolcnt.append(1)
        
        # 将索引限制在0到25范围内（对应A到Z）
        str1 += chr((symbolpool.index(symbol_hash_value) % 26) + 65)

print(symbolcnt)
print(str1)
