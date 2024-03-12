str1=input("enter the any String :")
if(str1[0]>='a' and str1[0]<='z'):
    a=(str1[0])
    a1=ord(a)-32
    print(chr(a1),end="")
    ctr=1
    while(ctr<len(str1)):
        ch=str1[ctr]
        print(ch,end="")
        ctr+=1
        
else:
    print("Your first letter of a string also a capital letter can not convert ")
    
