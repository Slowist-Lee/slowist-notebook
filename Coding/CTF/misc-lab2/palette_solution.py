# ：①从图像数据流中解码后的得到像素的在 初始 调色 板的 索引 Index0；② 根据 在初 始调 色板的索引Index0 得到像素值 P；③在新的调色板中找到像素 P 对应的索引 Index1；④如果索引Index1 为奇数，则嵌入位为 1，否则嵌入位是 0，每 8 位组装成一个字节，就提取出消息。

from PIL import Image
im = Image.open("D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lab2/palette.png")
r=[]
g=[]
b=[]
plst=[]
if im.mode == 'P':
    palette = im.getpalette()
    for i in range(256): # palette only has 8-bit color, so 2^8=256
        r=palette[3*i]
        g=palette[3*i+1]
        b=palette[3*i+2]
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        plst.append(Y) # original palette
    plst_sorted=sorted(plst)
    pixel_indices = list(im.getdata())
    width=im.size[0]
    height=im.size[1]
    flag=[]
    for i in range(height):
        for j in range(width):
            flag.append((plst_sorted.index(plst[pixel_indices[i*width+j]]))%2)
    flagstr="".join(map(str,flag))
    with open("palette_flag.txt", "w") as file:
        file.write(flagstr)      
    print("done")   
else:
    print("no palette")

# im.getdata() 返回图像的像素数据。对于P模式图像，每个像素值是一个索引，指向调色板中的某个颜色

