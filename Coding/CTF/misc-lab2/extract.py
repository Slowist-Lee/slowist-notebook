from blind_watermark import WaterMark
bwm1 = WaterMark(password_img=1, password_wm=1)
wm_extract = bwm1.extract('misc2miao.jpg', wm_shape=10,mode='str')
print(wm_extract)