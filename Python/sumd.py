def sp_sum(num):
    sumd=0
    while num>0:
        rem=num%10
        sumd+=rem
        num//=10
    return sumd
print(sp_sum(int(input("Enter a number:"))))
