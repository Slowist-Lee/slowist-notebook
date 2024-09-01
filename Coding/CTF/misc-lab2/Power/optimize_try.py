import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# 生成示例数据
xdata = np.linspace(0, 12, 1)
ydata = np.array()
# 拟合曲线
popt, pcov = curve_fit(func, xdata, ydata)

# 使用拟合参数计算拟合曲线的y值
y_fit = func(xdata, *popt)

# 计算实际值和拟合值的差别
difference = ydata - y_fit

# 打印拟合参数
print("Fitted parameters:", popt)

# 可视化实际数据和拟合曲线
plt.scatter(xdata, ydata, label='Data')
plt.plot(xdata, y_fit, color='red', label='Fit')
plt.legend()
plt.show()

# 可视化实际值和拟合值的差别
plt.plot(xdata, difference, label='Difference')
plt.legend()
plt.show()
