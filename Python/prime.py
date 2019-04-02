N=int(input("Input a number"))
count=0
i=0
while i<N:
    n=int(input("Input a number"))
    j=n/2
    k=0
    while j>2:
        if n%j==0 or n==1:
            j-=1
            k=1
    if k!=1:
        count=count+1
    i+=1
print(count)    
        
