A=[]
B=[]
r1=int(input("Enter the 1st matrix row numbers : "))
c1=int(input("Enter the 1st matrix column numbers : "))
r2=int(input("Enter the 2nd matrix row numbers : "))
c2=int(input("Enter the 2nd matrix column numbers : "))
if c1==r2:
    print("Elements of the 1st matrix are : ")
    for i in range(r1):
        row1=[]
        for j in range(c1):
            row1.append(int(input()))
        A.append(row1)
    print("1st Matrix : ",A)
    print("Elements of the 2nd matrix are : ")
    for i in range(r2):
        row2=[]
        for j in range(c2):
            row2.append(int(input()))
        B.append(row2)
    print("2nd Matrix : ",B)
    result=[]
    for i in range(r1):
        row3=[]
        for j in range(c2):
            row3.append(0)
        result.append(row3)
    print("Initial result matrix : ",result)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]+=A[i][k]*B[k][j]
    print("After Multiplication : ")
    for r in result:
        print(r)
else:
    print("Matrix Multiplication is not possible 1st matrix is a ",r1,"X",c1,"& 2nd matrix is",r2,"X",c2)

    
