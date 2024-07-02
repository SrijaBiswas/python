a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))
avg=(a+b+c)//3
print("The average is : ", avg)
if avg<40:
    print("Grade is : Fail")
elif avg>=40 and avg<=50:
    print("Grade is : C")
elif avg>50 and avg<=60:
    print("Grade is : B")
elif avg>60 and avg<=70:
    print("Grade is : B+")
elif avg>70 and avg<=80:
    print("Grade is : A")
elif avg>80 and avg<=90:
    print("Grade is : A+")
else:
    print ("Grade is : O")
