n=int(input("Enter the size of matrix: "))
mat1=[]
for i in range(0,n):
    temp=[]
    for i in range(0,n):
        x=int(input("Enter the element of first matrix: "))
        temp.append(x)
    mat1.append(temp)
    
mat2=[]
for i in range(0,n):
    temp1=[]
    for i in range(0,n):
        x=int(input("Enter the element of second matrix: "))
        temp1.append(x)
    mat2.append(temp1)
print("First matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat1[i][j], end=' ')
    print()
print("Second matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat2[i][j], end=' ')
    print()
print("Addition of matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat1[i][j]+mat2[i][j], end=' ')
    print()
print("Substraction of matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat1[i][j]-mat2[i][j], end=' ')
    print()    
    
print("Multiplication of matrices: ")
for i in range(0,n):
    for j in range(0,n):
        let=0
        for k in range(0,n):
            let=let+mat1[i][k]*mat2[k][j]
        print(let, end=' ')
    print()
print("Transporse of first matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat1[j][i], end=' ')
    print()
print("Transporse of second matrix is: ")
for i in range(0,n):
    for j in range(0,n):
        print(mat2[j][i], end=' ')
    print()
