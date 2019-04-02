st = input("Enter string:")
l = st.split(" ")
dic = {}
print(len(l))
l.sort()
for i in l:
    dic[i] = dic.get(i, 0) + 1
    # if i[0] == 'a':
    print(i)
