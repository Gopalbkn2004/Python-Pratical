import math
while(True):
    area=0
    print()
    print('MAIN MENU')
    print("----------")
    print("1. Volume of a cube")
    print("2. Volume of a Sphere")
    print("3. Volume of a Pyramid")
    print("4. Volume of a Cylinder ")
    print("5. Volume of a Triangle prism ")
    print("6. Volume of a Cone ")
    print("7. Volume of a Cuboid")
    print("8. Quit")
    print('-----------')
    opt=int(input("Enter the your option :"))
    if(opt==1):
        s=float(input("enter the side of the cube :"))
        volume=s*s*s
        print("Volume of cube is=>%.2f",volume)
    if(opt==2):
        r=float(input("enter the radius of the Sphere :"))
        volume=4/3*(math.pi*math.pow(r,3))
        print("Volume of Sphere is=>%.2f",volume)
    if(opt==3):
        b=float(input("enter the Base of the Pyramid :"))
        h=float(input("enter the Height of the pyramid :"))
        volume=(b*h)/3
        print("Volume of Pyramid is=>%.2f",volume)
    if(opt==4):
        r=float(input("enter the radius of the cylinder :"))
        h=float(input("enter the Height of the cylinder :"))
        volume=math.pi*math.pow(r,2)*h
        print("Volume of cylinder is=>%.2f",volume)
    if(opt==5):
        a=float(input("enter the area of the triangle :"))
        h=float(input("enter the Height of the triangle :"))
        volume=a*h
        print("Volume of triangle is=>%.2f",volume)
    if(opt==6):
        r=float(input("enter the radius of the cone :"))
        h=float(input("enter the height of the cone :"))
        volume=((math.pi*math.pow(r,2)*h))/3
        print("Volume of cone is=>%.2f",volume)
    if(opt==7):
        l=float(input("enter the length of the cuboid :"))
        b=float(input("enter the breath of the cuboid :"))
        h=float(input("enter the height of the cuboid:"))
        volume=l*b*h
        print("Volume of cuboid is=>%.2f",volume)
    elif(opt==8):
        break
    
