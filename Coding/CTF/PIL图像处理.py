#高中技术书 https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets/4179c16a-892b-43d6-b6c4-0cf1d97dcd3e.pkg/pdf.pdf
from PIL import Image
width=64 #行数
height=64 #列数
str1=""
def bw_judge(R,G,B):
    Gray_scale = 0.299 * R + 0.587 *G + 0.114 * B
    # https://zhuanlan.zhihu.com/p/421552912 FPGA灰度图像处理
    return Gray_scale<132 # 1 是白色，0是黑色
image=Image.open("D:/My Repository/slowist-notebook/docs/Coding/CTF/crypto_challenge1.png")
pixels=image.load()
symbolpool=[]
symbolcnt=[]
for row in range(13):
    for col in range(21):
        symbol=[[0 for i in range(height)]  for j in range(width)] # 一个存放符号的矩阵
        for i in range(width):
            for j in range(height):
                R,G,B = pixels[j+64*col, i+64*row]
                symbol[i][j]=int(bw_judge(R,G,B))
                l=len(symbolpool)
        # 检查符号是否已经在 symbolpool 中
        if symbol in symbolpool:
            idx = symbolpool.index(symbol)
            symbolcnt[idx] += 1
        else:
            symbolpool.append(symbol)
            symbolcnt.append(1)
        str1+=chr(symbolpool.index(symbol)+65)
print(symbolcnt)
print(str1)