listi=[]
listo=[]
n=int(input("Enter the limit: "))
for i in range(1,n+1):
      listi.append(i)
      listi.append((i**2))
      listo.append(listi)
      listi=[]
print(listo)
