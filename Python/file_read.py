f=open("E:\python\mytextfile.txt","w")
while True:
    text=""
    text=input("Input the text:")
    if text!="":
        f.write(text+"\n")
    else:break
f.close()
f=open("E:\python\mytextfile.txt","r")
for line in f:
    line=line.strip()
    print(line,end="")
    print()
f.close()
