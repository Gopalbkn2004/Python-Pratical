add=sub=mult=div=0
while(True):
    print()
    print("Main Menu ")
    print("______________")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Quit")
    print("______________")
    ch=input("enter your choice ")
    if(ch=='5'):
        break
    x=int(input("enter first number :"))
    y=int(input("enter second number:"))
    if(ch=='1'):
        add=x+y
        print("sum of %0.2f and %0.2f is:%0.2f"%(x,y,add))
    elif(ch=='2'):
        sub=x-y
        print("subtracting of %0.2f and %0.2f is:%0.2f"%(y,x,sub))
    if(ch=='3'):
        mult=x*y
        print("Multiplying of %0.2f and %0.2f is:%0.2f"%(x,y,mult))
    if(ch=='4'):
        if(x==0 or y==0):
            print("both number must be positive ")
        else:
            div=x/y
            print("Division of %0.2f and %0.2f is:%0.2f"%(x,y,div))
    
