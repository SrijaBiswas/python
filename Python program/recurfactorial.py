#Factorial of a number using recursion
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
x=int(input("Enter any Number :"))
if x<0:
    print("Factorial of a negative number is not possible !!!!!!")
elif x==0:
    print("Factorial of 0 is : 1")
else:
    print("Factorial of ",x,"is :",fact(x))
    
