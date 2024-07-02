from itertools import permutations
#per=permutations([1,2,3])
lst=list(input("Enter the list elements : "))
per=permutations(lst)
for i in list(per):
    print (i)
