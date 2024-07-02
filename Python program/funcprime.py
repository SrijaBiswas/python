#prime no checking
def prime(l,u):
    c=0
    p1=[]
    p2=[]
    for n in range(l,u+1):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    print("Not prime no: ",n)
                    p1.append(n)
                    break
            else:
                p2.append(n)
                print("The prime no: ",n)
                c=c+1
        else:
            print("Please enter the lower limit number >1")
    print("Total Prime Number : ",c )
    print("List of not Prime Number : ",p1 )
    print("List of Prime Number : ",p2 )
l=int(input("Enter lower limit no : "))
u=int(input("Enter upper limit  no : "))
prime(l,u)
