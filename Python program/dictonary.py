dic={
    "First Name" : "Srija",
    "Last Name" : "Biswas",
    "Age" : 21,
    "Sub":["Data Structure", "C++", "Java", "Python"]
    }
print(dic)
print(len(dic))
print(dic["Age"])
print(type(dic))
x=dic.keys()
print("Keys : ",x)
y=dic.values()
print("Values : ",y)
def root(n):
    l=lambda b:b**2
    b=lambda a:l(n)+2*a
    print("Square: ",l(n))
    print("a^2+2a :  ",b(n))
root(12)
lm=int(input("Enter input : "))
root(lm)

