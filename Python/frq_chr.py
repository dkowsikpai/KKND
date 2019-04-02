s1=input("Enter the string: ")
dic={}
for i in s1:
    dic[i]=dic.get(i,0)+1
print (dic)
