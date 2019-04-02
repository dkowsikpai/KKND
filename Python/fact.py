pro=1
def fact(i):
    if i==1:
        return i
    else:
        return i*fact(i-1)

n=int(input("Input a number:"))
if n<0:print("Enter a positive number")
elif n==0:print(1)
else:print(fact(n))
input()
