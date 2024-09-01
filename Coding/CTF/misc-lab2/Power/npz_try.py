import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
# 读取 NPZ 文件
data = np.load('attachment.npz')

# 查看包含的数组名称
print("Contained arrays:", data.files)

# 访问数组
print("index:", data['index'])
print("input:", data['input'])
print("output:", data['output'])
print("trace:", data['trace'])
trace=data['trace']
print(len(trace))
lst=[[] for _ in range(len(trace))]
for i in range(len(trace)):
    for j in range(13):
        lst[i].append(trace[j][i])

lst_avg=[]
for i in lst:
    lst_avg.append(round(sum(i)/len(i),2))

# 生成示例数据
xdata = np.linspace(0, 521, 1)
ydata = np.array(lst_avg)
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
