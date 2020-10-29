import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]

def lssin():
    y1=2*np.sin(0.5*np.pi*x+2)
    plt.title('sin(t)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def lsex():
    A=2
    a=0.6
    y4=A*a**x1
    plt.grid(True)
    plt.title('e^x')
    plt.stem(x1,y4)
    plt.show()

def  lsjy():
    def dwjy(t):
        r=np.where(t>=0.0,1.0,0.0)
        return r
    n=np.arange(-4,8)
    plt.ylim(0,2)
    plt.title('jieyue')
    plt.grid(True)
    plt.stem(n,dwjy(n))
    plt.show()

def lscj():
    def dwxl(temp):
        r=np.where(temp==0.0,1.0,0.0)
        return r
    m=np.arange(-4,8)
    plt.ylim(0,2)
    plt.title('chognji')
    plt.grid(True)
    plt.stem(m,dwxl(m))
    plt.show()

import sys
from PyQt5 import QtWidgets,QtGui,QtCore,Qt
app=QtWidgets.QApplication(sys.argv) #申明主程序
windows=QtWidgets.QWidget()
windows.resize(500,500)
windows.move(100,100)
"""
qr=windows.frameGeometry()
cp=QtWidgets.QDesktopWidget().availableGeometry().center()
qr.moveCenter(cp)
windows.move(qr.topLeft())
"""
windows.setWindowTitle('信号与系统') #添加窗口标题
btn = QtWidgets.QPushButton('离散正弦信号',windows) #设置按钮并给按钮命名
btn.setGeometry(200,150,100,50) #设置按钮位置和大小
btn.clicked.connect(lssin)
btn = QtWidgets.QPushButton('离散指数信号',windows)
btn.setGeometry(200,200,100,50) 
btn.clicked.connect(lsex)
btn = QtWidgets.QPushButton('离散阶跃信号',windows)
btn.setGeometry(200,250,100,50)
btn.clicked.connect(lsjy)
btn = QtWidgets.QPushButton('离散冲激信号',windows)
btn.setGeometry(200,300,100,50)
btn.clicked.connect(lscj)
windows.show()
sys.exit(app.exec_())