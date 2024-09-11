'''用python绘制函数图像'''
import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return 0.01*x**2+0.1*x

x=np.arange(0.0,20.0,0.1)
y=func1(x)

plt.plot(x,y)
plt.show()
