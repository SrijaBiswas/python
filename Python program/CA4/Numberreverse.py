print("Integer Reverse")
num=int(input("Enter the Integer : "))
rev=0
while num!=0:
    r=num%10
    rev=(rev*10)+r
    num//=10
print("Reverse Number is : ",rev)

