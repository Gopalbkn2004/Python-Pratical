l=['a','b','c']
l1=[]
l2=[]
def encoding():
 for i in range(0,3):
      l1.append(chr(ord(l[i])+10))
 print(l1)
 
def decoding():
 for j in range(0,3):
     l2.append(chr(ord(l1[j])-10))
 print(l2)
encoding()
decoding()
