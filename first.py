print("hello")
print("我是新分支")

print("再试试本地修改")
import numpy as np
import matplotlib.pylab as plt

def func(x):
    return np.array(x>0,dtype=np.int)

x=np.arange(-5.0,5.0,0.1)
#都是符合dec
#远端更新一个方法
import math
pi=math.pi

def circle_area():
    r=float(input('请输入半径：'))
    s=pi*r*r
    print('圆面积为：{:.2f}'.format(s))
    
circle_area()
