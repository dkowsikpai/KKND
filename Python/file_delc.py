f=open("E:\python\mytextfile.txt","r")
f2=open("E:\python\mytext.txt","w")
for line in f:
    h=0
    st=0
    word_list=line.split()
    for word in word_list:
        if word=="#":st=1
        else:h=0
        if st==1:
            print(word+" ",end="")
        else:
            h=1
            strl=word+" "
            print(strl)
            f2.write(strl)
    if h==1:f2.write("\n")
    print()
f2.close()
f.close()

