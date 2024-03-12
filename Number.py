import math
while(True):
    print()
    print("Main Menu")
    print("__________")
    print("1. Special number")
    print("2. Armstrong number")
    print("3. prine number")
    print("4. Automorphic number")
    print("5. Quit ")
    print("_________")
    opt=int(input("enter the your option :"))
    print()
    if(opt==1):
        n=int(input("enter a number to check special number :"))
        n1=n
        rem=sun=0
        while(n1>0):
            rem=n1%10
            n1=n1//10
            f=1
            for i in range(1,rem+1):
                f=f*i
            sum=sum+f
        if(n==sum):
            print("It is a special number ")
        else:
            print("It is not a special number ")
    elif(opt==2):
        n=int(input("Enter the number to check Armstrong number:"))
        n1=n
        rem=sum=0
        while(n1>0):
            rem=n1%10
            n1=n1//10
            sum=sum+math.pow(rem,3)
        if(n==sum):
            print("it is an Amstrong number ")
        else:
            print("Its is not an Amstrong number ")
    elif(opt==3):
        opt=0
        n=int(input("enter a number to check prime number :"))
        for i in range(2,n):
            if(n%i==0):
                opt=1
                break
            i=i+1
        if(opt==1):
            print("It is not a prime number")
        else:
            print("it is a prime number")
    elif(opt==4):
        n=int(input("enter the number to check Automorphic number :"))
        n1=n
        ctr=rem=sum=0
        while(n1>0):
            rem=n1%10
            n1=n1//10
            ctr+=1
        sqrnum=n*n
        lastdigit=count=0
        for i in range(i,ctr+1):
            rem=sqrnum%10
            lastdigit=lastdigit*10+rem
            sqrnum=sqrnum//10
            count+=1
        cttr=rem=ld=0
        for i in range(1,count+1):
            rem=lastdigit%10
            ld=ld*10+rem
            lastdigit=lastdigit//10
        if(n==ld):
            print("It is an Automorpic number")
        else:
            print("it is not an AutoMorphic number")
    elif(opt==5):
        break
    
