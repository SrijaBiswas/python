#add and delete items from a list
def newlist():
    n=int(input("Enter the number of elements : "))
    b=[]
    for i in range(1,n+1):
        a=int(input("Enter elements : "))
        b.insert(i,a)
        print(b)
    print("Final List : ",b)
    x=int(input("Enter the index value of the removal element : "))
    b.pop(x)
    print("List After deleting ", x," index value : ",b)
print(newlist())
    
