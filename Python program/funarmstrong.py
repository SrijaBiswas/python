#Armstrong number
def arm(l,u):
    for n in range(l,u+1):
        pow=len(str(n))
        sum=0
        num=n
        while n>0:
            r=n%10
            sum+=r**pow
            n//=10
        if num==sum:
            print("Armstrong number : ",num)
l=eval(input("Enter lower range : "))
u=eval(input("Enter upper range : "))
arm(l,u)
        
    
