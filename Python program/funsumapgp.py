#sum of natural number
def sumnatural(n):
    x=n*(n+1)/2
    y=(n*(n+1)*(2*n+1))/6
    z=x**2
    print("the Sum of the 1st  natural numbers : " ,x)
    print("the Sum of the square of 1st natural numbers : " ,y)
    print("the Sum of the cube of 1st natural numbers : " ,z)
n=eval(input("Enter range number : "))
sumnatural(n)
        
