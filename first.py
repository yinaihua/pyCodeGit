print("hello")
print("我是新分支")

print("再")
import numpy as np
import matplotlib.pylab as plt

def func(x):
    return np.array(x>0,dtype=np.int)

x=np.arange(-5.0,5.0,0.1)
y=func(x)

plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
print("测试")
#远端修改

