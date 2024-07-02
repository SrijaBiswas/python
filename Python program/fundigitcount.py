#digit count of a number
def dcount(a):
    c=0
    while a!=0:
        a//=10
        c+=1
    return c
x=int(input("Enter any Number : "))
print("The digits are : ",str(dcount(x)))
        
