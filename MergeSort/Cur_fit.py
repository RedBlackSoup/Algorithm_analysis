import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50) #在0 到 4 之间生成等差数列 ，共50个元素
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size) #正态分布 随机数组
ydata = y + y_noise

popt, pcov = curve_fit(func, xdata, ydata) #popt 数组为待求的三个参数, pcov 是参数的协方差矩阵
plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.plot(xdata, y, 'b-', label='data')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()