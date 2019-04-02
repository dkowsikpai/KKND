ph = {}


def add():
    print("--Add--")
    name = input("Enter the name:")
    no = input("Enter the contact:")
    if ph.get(name,0)!= 0:
        ph[name].append(no)
    else:
        ph[name] = []
        ph[name].append(no)
    return 0
    # print(ph)


def view():
    print("--View--")
    name = input("Enter the name:")
    if ph.get(name,0)!= 0:
        print(name,":",ph[name])
    else:
        print("no contact Found!!!")
    return 0


def update():
    print("--Update--")
    name = input("Enter the name:")
    if ph.get(name,0)!= 0:
        lt = ph[name]
        print(name,":",ph[name])
        ph[name] = []
        for i in lt:
            no = ""
            no = input("Enter the contact:")
            if no!= "":
                ph[name].append(no)
    else:
        print("no contact Fount!!!")
    return 0


def delc():
    print("--Delete--")
    name = input("Enter the name:")
    if ph.get(name,0)!= 0:
        ph.pop(name)
        print("Contact is successfully deleted")
    else:
        print("no contact Fount!!!")
    return 0


menu = """1.Add \n2.View \n3.Update \n4.Delete \n5.Exit"""
command = {1: add, 2: view, 3: update, 4: delc, 5: quit}
"""print("1. Add")        
print("2. View")
print("3. Update")
print("4. Delete")
print("5. Exit")"""
print(menu)
while True:
    c = int(input("Enter the choice:"))
    command[c]()
    """if c == 1:
        add()
    elif c == 2:
        view()
    elif c == 3:
        update()
    elif c == 4:
        delc()
    elif c == 5:
        print("--Exit--")
        break
"""