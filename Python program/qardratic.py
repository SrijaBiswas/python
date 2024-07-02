import math
print("Quardratic Euation is : ")
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
d=b**2-4*a*c
if d<0:
    print("Can't find a root because the d value is an Imaginary number")
else:
    x1=-b+math.sqrt(d)
    x2=-b-math.sqrt(d)
    if x1==x2:
        print("Root are equal :",x1)
    else:
        print("Root are : ",x1,x2)
    
