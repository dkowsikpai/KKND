listf=[0,1]
n=int(input("Enter the limit: "))
for i in range(2,n+1):
      listf.append(listf[i-2]+listf[i-1])
print(listf)
input()