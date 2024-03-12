import numpy as np
##a=np.array([[3,4,5,6],[9,7,6,4],[1,3,5,7]])
##b=np.array([[9,4,1,7],[3,4,7,4],[9,0,6,3]])
##c=a+b
##c1=np.add(a,b)
##print('using operator: \n',c)
##print('\nusing fuction: \n',c1)

##b=a.ravel()
##print(b)

##a1=np.arange(0,20,2).reshape((5,2))
##print(a1)
##print(np.sum(a1))
##print(a1.sum())

##print(a.nbytes)
##print(a.itemsize)
##
##
##b=np.arange(0,19,2)
##print(b)
##b1=b[::-1]
##print(b1)

##c=a+b
##print(c)

#a1=np.empty((5,5)).full((1,5),1)
##b1=np.full((5,5),1)
##for i in range(1,4,1):
##    for j in range(1,4,1):
##        b1[i][j]=3
##print(b1)

a=np.full((4,3),1)
b=np.full((3,5),2)
print('a Matrix values\n',a)
print('b Matrix values\n',b)
print('result:\n',a@b)


##a1=np.full((3,4),3)
##a2=a1.nbytes
##a3=a1.itemsize
##print(a1)
##print(a2)
##print(a3)

