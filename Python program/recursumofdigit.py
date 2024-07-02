#sum of digits of a number in a recursion
def dig_sum(n):
    if n==0:
        return 0
    else:
        return n%10+dig_sum(n//10)
x=int(input("Enter any Number :"))
print("Sum of the digits of ",x," number  is :",dig_sum(x))
    
