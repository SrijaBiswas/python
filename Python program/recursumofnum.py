#sum of n numbers in a recursion
def sum_num(n):
    if n<0:
        return n+sum_num(n+1)
    elif n>0:
        return n+sum_num(n-1)
    else:
        return n
x=int(input("Enter any Number :"))
print("Sum of the numbers :",sum_num(x))
    
    
