n=int(input("Enter the range of the pattern : "))
s=0
l=1
while l<=n:
    if s<l:
        print("* ",end="")
        s+=1
        continue
    if s==l:
        print(" ")
        l+=1
        s=0
print("\n")
s=""
for i in range(1,n+1):
    s+="*"
    print(s)
    
        
        
