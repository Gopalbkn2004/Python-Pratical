import matplotlib.pyplot as plt
##week=[1,2,3,4]
##onion=[40,80,100,50]
##plt.plot(week,onion,marker='X')
##plt.figure(figsize=(5,17))
##plt.grid(True)
##plt.xlabel("week")
##plt.ylabel("onion")
##plt.show()

import numpy as np
##x=np.arange(0.,10,0.1)
##a=np.cos(x)
##b=np.sin(x)
##plt.plot(x,a,'c',linewidth=2)
##plt.plot(x,b,'b',linewidth=5,linestyle=':')
##plt.show()

##fib=[0,1,1,2,3,5,8,13,21,34]
##a=np.sqrt(fib)
##plt.figure(figure=(15,7))
##plt.plot(range(1,11),fib,'co',markersize=7,linestyle='solid',markeredgecolor='r',linewidth=4)
##plt.plot(a,'yo',markersize=3,linestyle='solid', markeredgecolor='k',linewidth=2)
##plt.show()

##a=[1,0.5,3,4]
##b=[20,30,40,50]
##plt.scatter(a,b,c='blue',marker='*',alpha=0.6,s=190)
##plt.show()


##x=np.random.randint(1,100,size=(100,))
##y=np.random.randint(1,100,size=(100,))
##plt.scatter(x,y,color='b')
##plt.xlabel("x values")
##plt.ylabel("y values")
##plt.show()


info=['gold','silver','bronze','total']
aust=[80,59,59,198]
india=[26,20,20,66]
plt.bar(info,aust,color=['b','g','k','y'])
plt.bar(info,india,color='red')
plt.show()



