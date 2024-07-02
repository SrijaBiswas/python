s=[]
print("Selection Sort : ")
n=int(input("Enter the elements numbers : "))
for i in range(n):
    s.append(int(input()))
print(s)
for step in range(n):
    mid=step
    for i in range(step+1,n):
        if s[i]<s[mid]:
            mid=i
    s[step],s[mid]=s[mid],s[step]
print(s)
