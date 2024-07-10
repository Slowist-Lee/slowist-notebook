from blind_watermark import WaterMark

bwm1 = WaterMark(password_wm=1, password_img=1)

try:
    bwm1.extract(filename='chal.png', wm_shape=(64, 64), out_wm_name='chaltry.png')
except AssertionError as e:
    print(f"Error: {e}")
