import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,8])
y=np.array([3,10])
plt.plot(x,y,marker='*',color='b',linewidth=2.5)
plt.grid()
plt.show()


x=np.array([4,8])
y=np.array([9,10])
plt.plot(x,y,marker='o',color='r',ms=10,ls=':',mec='b',mfc='y')
plt.show()

a=[1,2,3,4]
b=[2,4,6,8]
plt.xlabel("some values")
plt.ylabel("download values")
plt.plot(a,b,marker='o')
plt.show()
