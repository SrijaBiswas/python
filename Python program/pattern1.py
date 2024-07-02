n=int(input("Enter the row number of the pattern : "))
for i in range(0,n):
    print(' * '*(i+1))
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print(" * ",end=" ")#print(k,end=" ")print(i,end=" ")print(j,end=" ")
    print("\r")
x=input("Enter a string for reverse and check is it palindrom or not : ")
rev=x[: :-1]
print(x,"Reverse is : ",rev)
if rev==x:
    print("Palindrom String")
else:
    print("Not palindrom")

