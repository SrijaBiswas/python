#create 2 separate list for negative and positive numbers form a list
lst=[]
lstp=[]
lstn=[]
n=int(input("Enter the range : "))
for i in range(0,n):
    l=int(input())
    lst.append(l)
print(lst)
for j in range(len(lst)):
    if lst[j]>=0:
        print("Positive number : ",lst[j])
        lstp.append(lst[j])
    else:
        print("Negative number : ",lst[j])
        lstn.append(lst[j])
print("Positive number list : ",lstp)
print("Negative number list : ",lstn)
lstp.sort()
lstn.sort()
print("Positive number sorted list : ",lstp)
print("Negative number sorted list : ",lstn)
