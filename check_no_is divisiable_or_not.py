a=int(input("Enter First number :- "))
b=int(input("Enter Second number :- "))
if (a>b and (a%b==0) ):
    print(a/b)
 
elif (a<b):
    a=a+b
    b=a-b
    a=a-b
    if (a>b and (a%b==0)):
          print(a/b)
    else:
        print("Not Divisible")
else:
    print("Not Divisible")
