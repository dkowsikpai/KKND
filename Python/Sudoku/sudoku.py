import pickle
def rowcorrect(l2):
        # counter as set
        for i in l2:
                s = set()
                for j in i:
                       s.add(j)
                if len(s) != 9:
                        return False
        return True
def boxcorrect(l2):
        # counter as set
        s = set()
        for i in l2:
                for j in i:
                       s.add(j)
        
        if len(s) != 9:
                return False
        return True

def transpose(l2):
        # transpose
        # default 2-D array
        lt = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]
              ]
        for i in range(0,9):
                for j in range(9):
                        lt[j][i] = l2[i][j]
        return lt


def boxerl(l):
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        b7 = []
        b8 = []
        b9 = []
        
        for i in range(9):
                b1t = []
                b2t = []
                b3t = []
                b4t = []
                b5t = []
                b6t = []
                b7t = []
                b8t = []
                b9t = []                
                for j in range(9):
                        if i<=2 and j <= 2:
                                b1t.append(l[i][j])
                        elif i<=2 and 2<j<=5:
                                b2t.append(l[i][j])
                        elif i<=2 and j<=8:
                                b3t.append(l[i][j])
                        elif 2<i<=5 and j<=2:
                                b4t.append(l[i][j])
                        elif 2<i<=5 and 2<j<=5:
                                b5t.append(l[i][j])
                        elif 2<i<=5 and j<=8:
                                b6t.append(l[i][j])
                        elif 5<i<=8 and j<=2:
                                b7t.append(l[i][j])
                        elif 5<i<=8 and 2<j<=5:
                                b8t.append(l[i][j])
                        elif 5<i<=8 and j<=8:
                                b9t.append(l[i][j])

                if len(b1t) !=0 :b1.append(b1t)
                if len(b2t) !=0 :b2.append(b2t)
                if len(b3t) !=0 :b3.append(b3t)
                if len(b4t) !=0 :b4.append(b4t)
                if len(b5t) !=0 :b5.append(b5t)
                if len(b6t) !=0 :b6.append(b6t)
                if len(b7t) !=0 :b7.append(b7t)
                if len(b8t) !=0 :b8.append(b8t)
                if len(b9t) !=0 :b9.append(b9t)
                
                
        """print(b1)
        print(b2)
        print(b3)
        print(b4)
        print(b5)
        print(b6)
        print(b7)
        print(b8)
        print(b9)"""
        if boxcorrect(b1) and boxcorrect(b2) and boxcorrect(b3) and boxcorrect(b4) and boxcorrect(b5) and boxcorrect(b6) and boxcorrect(b7) and boxcorrect(b8) and boxcorrect(b9):
                return True
        else:
                return False

def sudoku(l):
        for i in range(9):
                print(l[i])
        if rowcorrect(l) and rowcorrect(transpose(l)) and boxerl(l):
                print("Congratulations")
        else:
                print("try again")   

print("-----------Welcome to sudoku Evaluvator--------")
try:
        f1 = open("sudoku.txt", "r")
        lines = f1.readlines()
        l1 = []
        for line in lines:
                l1t = []
                l1t = list(map(int, line.split(" ")))
                l1.append(l1t) 
        f1.close()
        f1 = open("sudoku2.bin", "wb")
        pickle.dump(l1, f1)
        f1.close()
        f = open("sudoku2.bin", "rb")
        l = pickle.load(f)
        f.close()
        # l[0][0] = 9
        # l[0][1] = 9
        sudoku(l)
except:
        f1 = open("sudoku.txt", "w")
        f1.write("Write the sudoku here in space seperated format. Next row must start in new line. Befor pasting delete this line and write fom the first line of this file")
        print("See the current directory and open sudoku.txt file and restart the program.")
        f1.close()
input("Press enter key to exit")
