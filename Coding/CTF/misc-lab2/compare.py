from PIL import Image, ImageChops

# 打开两张图像
img1 = Image.open('chal.png')
img2 = Image.open('REAL.png')

# 计算图像差异
diff = ImageChops.difference(img1, img2)

# 显示差异图像
diff.show()

# 保存差异图像
diff.save('differ1.png')
