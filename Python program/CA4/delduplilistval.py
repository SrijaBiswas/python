lst=[]
n=int(input("Input the list elements no : "))
for i in range(n):
    lst.append(input("Enter element : "))
print("Original list is : ",lst)
lst1=[]
print("Unique list elemnets are : ")
for i in lst:
    if i not in lst1:
        print(i)
        lst1.append(i)
print("After removing duplicate values from the list : ",lst1)
