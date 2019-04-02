k=[]
for i in range(1000,3001):
    j=str(i)
    if (int(j[0])%2==0) and (int(j[1])%2==0) and (int(j[2])%2==0) and (int(j[3])%2==0):
        k.append(j)
print(",".join(k))
