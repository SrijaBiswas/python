b=[]
print("Bobble Sort : ")
n=int(input("Enter the elements numbers : "))
for i in range(n):
    b.append(int(input()))
print(b)
for i in range(len(b)):
    for j in range(len(b)-i-1):
        if b[j]>b[j+1]:
            b[j],b[j]=b[j+1],b[j+1]
print(b)
