import numpy as np
import matplotlib.pylab as plt
def u(t):
    y = t > 0  # numpy数组中的每个元素都与0比较大小，得到一个布尔型numpy数组
    return y.astype(np.int)   #　astype()方法将numpy数组的布尔型转换为int型

t = np.arange(-5.0,5.0,0.1)  # 生成一个numpy数组，范围是(-5.0,5.0),步长为0.1
y = u(t)
plt.plot(t,y)
plt.ylim(-0.1,1.1)
plt.show()
