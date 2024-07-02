#krisnamurti number 145=1!+4!+5!
def kri(a):
    num=a
    sum=0
    while a!=0:
        r=a%10
        fact=1
        for i in range(r,1,-1):
            fact*=i
        sum+=fact
        a//=10
    if sum==num:
        return 1
    else:
        return 0
x=int(input("Enter any Number : "))
if kri(x)==1:
    print("Krisnamurti number : ",x)
else:
    print("Not a Krisnamurti number : ",x)
