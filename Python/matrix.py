def printMulti(i,m):
    j=1
    while j<=m:
        #print ('%4d'%(i*j),end='')
        print ((i*j),"\t",end='')
        j=j+1
    print('')
        
def printTable(n,m):
       i=1
       while i<=n:
              printMulti(i,m)
              i=i+1
       
def inputTable():
    print ("Give the dimension of the table (n x m)")
    printTable(int(input("n = ")),int(input("m = ")))


inputTable()
input()
