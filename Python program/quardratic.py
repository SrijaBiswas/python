import cmath
print("Roots of Quardratic equation  : ")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=(b**2)-4*a*c
x1=(-b-cmath.sqrt(d))/(2*a)
x2=(-b+cmath.sqrt(d))/(2*a)
if d>=0:
    if d==0:
        print("The  roots are equal so root is: ",x1)
    else:
        print("The  roots are ",x1," & ",x2)
else:
    print("The imaginary roots are ",x1," and ",x2,".".format(x1,x2))
        
        
