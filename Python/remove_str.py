s1=input("Enter main string: ")
s2=input("Enter sub string: ")
k=s1.find(s2)
s3=s1[:k]+s1[k+len(s2):]
print("The required string is "+s3)
