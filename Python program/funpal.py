#Palindrom number 121 reverse is also 121
def pal(a):
    num=a
    rev=0
    while a!=0:
        r=a%10
        rev=rev*10+r
        a//=10
    if rev==num:
        return 1
    else:
        return 0
x=int(input("Enter any Number : "))
if pal(x)==1:
    print("Palindrom number : ",x)
else:
    print("Not a palindrom number : ",x)
