str1="Gopal1"
for i in str1:
    if(i>="A" and i<="Z" and i>='a' and i<='z' and i>='0' and i<='9'):
        d=1
       # print(i)
    else:
        d=0
        #print(i)
        break

if(d==0):
    print("False")
else:
    print("true")
        
