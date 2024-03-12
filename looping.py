##for i in range(10,15):
##    print(i,end=" ")
##else:
##    print("Range limit over")

#infinite Looping
#war=1
#while(war==1):
#    num=int(input("enter a number :"))
#    print("you have entered ",num)
##Write a program to print a table 2 to 4 using nested for Loop
#for i in range(2,5):
#    t=1
#    print()
#    print("Math table :",i)
#    for j in range(1,11):
#        t=i*j
#        print("%d  *  %d  =%d" %(i,j,t))
##write a program to print using for else statment to search all the prine number between 2 to 20
#print("prime no. are ",end=" ")
#for num in range(2,20+1):
#    if(num>1):
#        for i in range(2,num):
#            if(num%i==0):
#                break
#        else:
#            print(num,end=" ")
        
#Write a program to find multiplication table from 1 to 10 nested while loop
##a=1
##end=10
##while(a<=10):
##    t=1
##    print()
##    print("Math table :",a)
##    a1=1
##    while(a1<=end):
##        t=a*a1
##        print("%d  *  %d  = %d"%(a,a1,t))
##        a1=a1+1
##        
##    a+=1

#write a program to find factorial of all number between 1 to 10 using for loop
#sum=1
#for i in range(1,11):
#    sum*=i
#    print("factorial of %d is %d" %(i,sum))
#write a program to compute the average of 10 real number
#add=0
#for i in range(1,11):
#    add+=i
#    ave=add/i
#    print("Average of %d is  %.2f"%(add,ave))
#write a program  to accept a an integer no. and reverse a integer no.
##a=int(input("enter the number:"))
##b=0
##while(a!=0):
##    d=int(a%10)
##    b=b*10+d
##    a=a//10
##print(b)
#print * pattern
##n=int(input("enter the number of grow :"))
##d=n
##while n>=0:
##    x="*" *n
##    print(x)
##    n-=1
##i=1
##while i<=d:
##    print("*"*i)
##    i+=1

#Write a program to sum all the digits
##n=int(input("enter the end number :"))
##sum=0
##while n!=0:
##    sum=sum+n
##    n-=1
##print(sum)
#write a program to find a factorial
##fact=ctr=1
##n=int(input("enter the any number :"))
##while(ctr<=n):
##    fact=fact*ctr
##    ctr+=1
##print("factorial of %d is %.3f"%(n,fact))

#write a program to generate and display all the armstrong number betwwen 1 to 500
#write a program sum of the following series s=x-x**2/3+x**3/5
##n=int(input("enter the end number :"))
##x=int(input("enter the value:"))
##d=0
##j=1
##a=1
##for i in range(1,n*2,2):
##    if(a%2==0):
##        d=(d-((x**j)/i))
##    else:
##        d=(d+((x**j)/i))
##    a+=1
##    j+=1
##print(d)
#write a program to print a series
#for i in range (0,6):
#    for j in range(0,i):

##i=1
##while(i<6):
##    j=1
##    while(j<=i):
##        print(i,end=" ")
##        j+=1
##    i=i+1
##    print()    
# wite a program using module and create a file "text" in a current directory or a working directory to create a module for add two number and find sum of two number
def Addtwonumber():
    x=int(input("enter the first number:"))
    y=int(input("enter second number:"))
    result=x+y
    print("sum of %d and %d is %d"%(x,y,result))

def length(str):
    count=0
    for i in str:
         count+=1
    print(count)


def Twonum(x,y):
    if(x>y):
        result=x-y
    else:
        result=y-x
    return result
