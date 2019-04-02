def adds():
    suma=(int(input("Num1:"))+int(input("Num2:")))
    print (suma)
def sub():
    suma=(int(input("Num1:"))-int(input("Num2:")))
    print (suma)
def mul():
    suma=(int(input("Num1:"))*int(input("Num2:")))
    print (suma)
def div():
    suma=(int(input("Num1:"))/int(input("Num2:")))
    print (suma)

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
while True:
    k=int(input("Enter your choice:"))
    if k==1:adds()
    elif k==2:sub()
    elif k==3:mul()
    elif k==4:div()
    elif k==5:
        break
