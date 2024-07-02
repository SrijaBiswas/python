l=int(input("Enter lower range :"))
u=int(input("Enter upper range :"))
print("prime numbers between",l," and ",u," are : ")
c=0
for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
                c=c+1
                print(n)
print("print total prime number in the range ",l," & ",u," is : ",c)
    
