lists=input("Enter the string:").split(" ")
listn=[]
k=""
for i in lists:
      k=k.replace(k,k+" "+(i[0].upper()+i[1:].lower()))
print(k.strip(" "))
