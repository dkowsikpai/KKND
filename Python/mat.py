print("Enter the order of matrix")
n=int(input("n= "))
print("Enter the first matrix")
mat1=[]
mat2=[]
for j in range(n):
    mattemp=[]
    mattemp=list(map(int,input().split(" ")))
    mat1.append(mattemp)
print("Enter the second matrix")
for j in range(n):
    mattemp=[]
    mattemp=list(map(int,input().split(" ")))
    mat2.append(mattemp)

    
#print(mat1)
#print(mat2)
m=len(mat1)
n=len(mat1[0])
mat3=[]
mat=[]
temp=0
for i in range(m):
    mat3=[]
    temp=0
    for j in range(n):
        for k in range(n):
            temp+=mat1[i][k]*mat2[k][j]
            #print(temp)
        mat3.append(temp)
        temp=0
    mat.append(mat3)
for i in range(m):
    print(mat[i])
