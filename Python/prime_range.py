def prime(u,v):
    p=[]
    k=0
    for i in range(u,v+1):
        k=0
        for j in range(2,round(i/2)):
            if i%j==0:
                k=1
                break
        if k==0:
            p.append(i)
    return p 
print(prime(int(input("Enter a lower range:")),int(input("Enter a lower range:"))))
