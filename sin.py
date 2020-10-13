import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x=np.arange(0,2*np.pi,0.01)
y=np.sin(x*2)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("图像标题")
plt.show()