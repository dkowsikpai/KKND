import pickle
f = open("E:\python\mytextfile.pkl", "wb")
dic = {} # {1:"abc", 2: "def", 3: "ghi"}
while True:
    text = ""
    text = input("Input the Key:")
    if text != "":
        dic[text] = input("Enter the value:")
    else: break
# st=i+":"+dic[i]+"\n
pickle.dump(dic,f)
f.close()
f = open("E:\python\mytextfile.pkl", "rb")
dic1 = pickle.load(f)
print(dic1)
f.close()
