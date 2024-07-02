lst=[]
n=int(input("Input the list elements no : "))
for i in range(n):
    lst.append(int(input("Enter element : ")))
print("Original list is : ",lst)
lst.sort()
print("After sorting : ",lst)
if lst[-1]==lst[-2]:
    print("The second Largest Number is :",lst[-3])
else:
    print("The second Largest Number is :",lst[-2])
