import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
t = np.arange(-10.0, 10.0, 0.01)
y=np.sin(t)/t
plt.plot(t,y)
plt.xlabel("t")
plt.ylabel("y")
plt.title("抽样函数")
plt.show()