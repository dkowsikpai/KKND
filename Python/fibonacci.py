def fibo(n):
        if n<=1:
                return(n)
        else:
                return(fibo(n-1)+fibo(n-2))

num=int(input("Enter a number:"))
for j in range(num):
        print(fibo(j))
        
