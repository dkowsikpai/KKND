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
lg=0
for i in s1:
    if i not in s2:
        s1=repl(s1,"#",lg)#replacing all the charecters once 
        s2=s2+i
    lg+=1
ind=""
print(s1)
k=len(s2)
for j in range(0,k):
    s3+="1"#setting the counting variable to one
    ind+="1"

i=""
for i in s1:
    if i=="#":
        continue
    else:
        l=s2.index(i)
        p=str(int(s3[l])+1)
        if int(p)>9:
                ind=repl(ind,str(int(ind[l])+1),l)
        #print(p)
        s3=repl(s3,p,l)
        #s3[l]=str(p)



print ("The frequency of the charecters are:")
print("[",end="")
j=0
z=0
for i in ind:
    print(s2[z]+":",end="")
    for k in range(0,int(i)):
        print (s3[j],end="")
        j+=1
    print("  ",end="")
    z+=1
print("]")
#print(s2)
print(ind)

    
