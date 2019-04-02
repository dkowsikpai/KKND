def repl (str1,str2,l):
    ret=""
    ret=str1[:l]+str2+str1[l+len(str2):]
    return ret

s1=input("Enter the string: ")
s2=""
s3=""
l=0
k=0
p=""
sp=" "
space=0
for i in s1:
    if i not in s2 and i not in sp:
        s1=s1.replace(i,"#",1)#replacing all the charecters once 
        s2=s2+i
#print(s1)
k=len(s2)
for j in range(0,k):
    s3+="1" #setting the counting variable to one
i=""
for i in s1:
    if i=="#":
        continue
    else:
        l=s2.find(i)
        if l!=-1:
            p=str(int(s3[l])+1)
        else: space+=1
        #print(p)
        s3=repl(s3,p,l)
        #s3[l]=str(p)



print ("The frequency of the charecters are:")
print("[",end="")
j=0
for i in s2:
    print (i+" : "+s3[j]+"  ",end="")
    j+=1
print("]")
print("Number of spaces between charecters : " +str(space))
#print(s2)
#print(s3)
input()
