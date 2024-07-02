#Neon number a=9;9*9=81;8+1=9
def neo(a):
    num=a
    sq=a*a
    sum=0
    while sq!=0:
        r=sq%10
        sum+=r
        sq//=10
    if sum==num:
        return 1
    else:
        return 0
x=int(input("Enter any Number : "))
if neo(x)==1:
    print("Neon number : ",x)
else:
    print("Not a Neon number : ",x)
