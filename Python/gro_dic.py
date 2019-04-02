it_db={}
while True:
    it=""
    it=input("Enter the items:")
    if it!="":
        it_db[it]=int(input("Enter the price:"))
    else: break
it_bt={}
print("-------Purchase--------")
while True:
    it=""
    it=input("Enter the items:")
    if it!="":
        it_bt[it]=int(input("Enter the quantity:"))
        it_bt[it]=it_bt[it]*it_db[it]
    else: break
lt=it_bt.keys()
Tsum=0
for i in lt:
    Tsum+=it_bt[i]
    print(i," : ",it_bt[i])
print("Grand Total: ",Tsum,"/-")
