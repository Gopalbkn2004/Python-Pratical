# fabonic series 
'''x1=int(input("enter the end value:"))
"""Prints the Fibonacci series up to n."""
a,b = 0,1
while a < x1:
    print(a, end=' ')
    a, b = b, a + b'''
# fabonic series
'''a, b = 0, 1
x1=int(input("enter the value:"))
for _ in range(x1):
    print(a)
    a, b = b, a + b
    #temp = a + b
    #a = b
    #b = temp
   '''

#print table using nested while loop
'''n=1
while(n<=10):
    print("table of ",n)
    i=1
    while(i<=10):
        print(n,"x",i,"=",n*i)
        i=i+1
    n=n+1
'''
#wap to check prime nnumber or not
'''n=int(input("Enter the number:"))
a=0
for i in range(2,n):
    if(n%i==0):
        a=1
        break;
if(a==1):
     print("it is not prime number")
else:
    print("it is  prime number")'''
               
#print series 12,32,52,72 etc
'''n=int(input("enter the value (end)power of series:"))
s=0
i1=0
for i in range(0,n):
    for j in range(0,i+1):
        s=j*20+12
        print(s)
        i1=s+i1
    print(" ")
print("sum of series:",i1)'''


'''
marks=int(input("enter the marks :"))
if(marks>=91 and marks<=100):
    print("A1")
    print("10.0")
elif(marks>=81 and marks<=90):
    print("A2")
    print("9.0")
elif(marks>=71 and marks<=80):
    print("B1")
    print("8.0")
elif(marks>=61 and marks<=70):
    print("B2")
    print("7.0")
elif(marks>=51 and marks<=60):
    print("C1")
    print("6.0")
elif(marks>=41 and marks<=50):
    print("C2")
    print("5.0")
elif(marks>=33 and marks<=40):
    print("D")
    print("4.0")
elif(marks>=212 and marks<=32):
    print("E1")
    print("0.0")
elif(marks>=0 and marks<=20):
    print("E2")
    print("0.0")
else:
    print("invalid number")'''

#series 1+ X + X*X + X*X*X

'''x=int(input("enter the value :"))
n=int(input("enter the value power of series:"))
s=0
for j in range(0,n):
    y=pow(x,j)
    s=s+y
    print(y)

print("sum of the series",s)'''

#prime number or not
'''n=int(input("ENter the number:"))
a=0
if(n==1 or n==0):
    print(n," is not a prime number")
else:
    for i in range(2,n):
        if(n%i==0):
            a=1
            break;
    if(a==1):
        print("it is not prime number")
    else:
        print("it is  prime number")
'''
#reverse number
n=int(input("ENter the number:"))
a = n
reverse = 0
while n >0:
    remainder = n % 10
    reverse = (reverse * 10) + remainder
    n = n//10
print(reverse)

#wap find da hra of calculate
'''eno=int(input("enter the employe no.:"))
ename=(input("enter the name of employe:"))
sal=int(input("enter the salary:"))
if(sal<=10000):
    da=(sal*30)/100
    hra=(sal*10)/100
elif(sal>10000 and sal<=20000):
    da=(sal*40)/100
    hra=(sal*15)/100
elif(sal>20000 and sal<=30000):
    da=(sal*50)/100
    hra=(sal*20)/100
elif(sal>30000):
    da=(sal*60)/100
    hra=(sal*25)/100

print(eno,ename,da,hra)
gross=sal+da+hra
print("GROSS SALARY:",gross)'''
# wap to find area of circle,rectangle,square
'''while(True):
    area=0
    print()
    print('MAIN MENU')
    print("----------")
    print("1. Area of circle")
    print("2. Area of a rectangle")
    print("3. Area of a Square")
    print("4. Quit")
    print('-----------')
    opt=int(input("Enter the your option :"))
    if(opt==1):
        r=int(input("Enter the radius of circle :"))
        area=3.14*pow(r,2)
        print("area of circle :",area)
    elif(opt==2):
        l=int(input("Enter the length of ractangle :"))
        w=int(input("Enter the width of ractangle :"))
        area=w*l
        print("area of rectangle:",area)
    elif(opt==3):
        a=int(input("Enter the area of square :"))
        area=pow(a,2)
        print("area of Square :",area)
    elif(opt==4):
        break
    else:
        print("invalid entry")'''

#wap to evalute power of series 2power/factorial
'''x=int(input("Enter the value of x :"))
n=int(input("Enter the value of N :"))
sum1=0
for i in range(0,n+1):
    a=pow(x,i)
    fact=1
    for j in range(1,i+1):
        fact=j*fact
    sum1=(a/fact)+sum1
print(sum1)'''
   
#wap (1)+(1+2)+(1+2+3)+(1+2+3+4)
'''n=int(input("Enter the value of N :"))
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=j+sum
print(sum)'''
#discount sale market
'''discount=0
additionaldiscount=0
add=0
pamt=float(input("enter the purchase amount:"))
if(pamt>=2000 and pamt<=5000):
    discount=400
elif(pamt>5000 and pamt<=10000):
    discount=800
elif(pamt>10000 and pamt<=20000):
    discount=1000
elif(pamt>20000 ):
    discount=2000
    additionaldiscount=pamt*3/100
    add=3
td=discount+additionaldiscount
netamt=pamt-td
print("=====================================")
print("purchase amount is:",pamt)
print("discount amount is: ",discount)
print(add,"% additional discount is:",additionaldiscount)
print("total discount is: ",td)
print("net amount is: ",netamt)'''

#GEOMETRICAL SHAPES
'''import math
while(True):
    area=0
    print()
    print('MAIN MENU')
    print("----------")
    print("1. Volume of a cube")
    print("2. Volume of a Sphere")
    print("3. Volume of a Pyramid")
    print("4. Volume of a Cylinder ")
    print("5. Volume of a Cuboid")
    print("6. Quit")
    print('-----------')
    opt=int(input("Enter the your option :"))
    if(opt==1):
        s=float(input("enter the side of the cube :"))
        volume=s*s*s
        print("Volume of cube is=",volume)
    elif(opt==2):
        r=float(input("enter the radius of the Sphere :"))
        volume=4/3*(math.pi*math.pow(r,3))
        print("Volume of Sphere is=",volume)
    elif(opt==3):
        b=float(input("enter the Base of the Pyramid :"))
        h=float(input("enter the Height of the pyramid :"))
        volume=(b*h)/3
        print("Volume of Pyramid is=",volume)
    elif(opt==4):
        r=float(input("enter the radius of the cylinder :"))
        h=float(input("enter the Height of the cylinder :"))
        volume=math.pi*math.pow(r,2)*h
        print("Volume of cylinder is=",volume)
    elif(opt==5):
        l=float(input("enter the length of the cuboid :"))
        b=float(input("enter the breath of the cuboid :"))
        h=float(input("enter the height of the cuboid:"))
        volume=l*b*h
        print("Volume of cuboid is=",volume)
    elif(opt==6):
        break
    else:
        print("PLEASE ENTER CORRECT VALUE")'''





