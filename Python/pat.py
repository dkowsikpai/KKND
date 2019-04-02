
# Question 1
n = int(input("Input the number of & required:"))
m = int(((n-1)/2)+1)
j = 1
for i in range(m):
    # for k in range(i):  # replace m by 4
    print("\t"*i, end="")
    # for i in range(n-j+1):  # replace n-j+1 by 8-j
    print("&\t"*(n-j+1), end="")
    print()
    j = j+2

# Question 2
n = int(input("Input the number of rows required:"))
for i in range(n):
    print("\t", end="")
print("&")
for i in range(1, n):
    for j in range(n-i):
        print("\t", end="")
    print("&", end="")
    for k in range(i):
        print("\t\t", end="")
    print("&",end="")
    print()
for i in range(2*n+1):
    print("&\t", end="")

input() 
