term=10
result=list(map(lambda x:2**x, range(term)))
print("The total terms: ",term)
for i in range(term):
    print("2 raised to power",i," is : ",result[i])
print("List of the powers : ",result)
            
decimal=int(input("Enter the decimal value : " ))
print("The decimal value of ",decimal," is : ")
print(bin(decimal)," in binary.")
print(oct(decimal)," in octal.")
print(hex(decimal)," in hexadecimal.")
