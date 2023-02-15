dic1={}
tup1=()
list1=[]
for i in range(1,10):
    for j in range(1,10):
        dic1[(i,j)]=" "
for i in range(1,10):
    tup2=()
    tup3=()
    for j in range(1,10):
        tup2+=((i,j),)
        tup3+=((j,i),)
    tup1+=(tup2,)
    tup1+=(tup3,)
for i in range(1,10,3):
    for j in range(1,10,3):
        tup4=()
        for k in range(i,i+3):
            for l in range(j,j+3):
                tup4+=((k,l),)
        tup1+=(tup4,)
num_type="quesn"

class Player1:
    def __init__(self,dic1,tup1,num_type):
        self.dic1=dic1
        self.tup1=tup1
        self.num_type=num_type

    def Sudoku(self):
        print("Choose the cell you want to put number in.")
        while True:
            cell=input()
            if cell == "start":
                return "Start"
            elif cell[0]!="(" or cell.count(",")!=1 or cell[cell.index(",")-1]=="(" or cell[cell.index(",")+1]==")" or cell[-1]!=")":
                print("Give input only in \"(row number,column number)\" this format.")
            elif len(cell[1:-1].split(",")[0])>1 or ord(cell[1:-1].split(",")[0])<48 or ord(cell[1:-1].split(",")[0])>57:
                print("Choose row numbers only between 1-9.")
            elif len(cell[1:-1].split(",")[1])>1 or ord(cell[1:-1].split(",")[1])<48 or ord(cell[1:-1].split(",")[1])>57:
                print("Choose column numbers only between 1-9.")
            elif self.num_type=="ans" and tuple(map(int, cell[1:-1].split(","))) in list1:
                print("Choose blank cells that were given to you after the puzzle was set only.")
            else:
                break
        cell = tuple(map(int, cell[1:-1].split(",")))
        print("Put the number.")
        while True:
            n = input("")
            if n=="back":
                return "back"
            elif n==" ":
                break
            elif len(n)!=1 or ord(n[0])<48 or ord(n[0])>57:
                print("Choose only integers between 1-9.")
            else:
                break
        if n!=" ":
            n=int(n)
            list1.append(cell)
        else:
            n=" "
            list1.remove(cell)
        if self.num_type=="quesn":
            self.dic1[cell] = "\033[1m" + str(n) + "\033[0m"
        else:
            self.dic1[cell] = "\033[31m" + str(n) + "\033[0m"
        if " " not in self.dic1.values():
            for i in self.dic1:
                for j in self.tup1:
                    if i in j:
                        for k in j:
                            if k!=i:
                                if self.dic1[i] == self.dic1[k]:
                                    return "Not solved"
            return "Solved"

    def table(self):
        print("   1  2  3  4  5  6  7  8  9")
        for i in range(1,11):
            print("   ", end="")
            for j in range(9):
                if i==4 or i==7:
                    print("\033[31m" + "__ " + "\033[0m", end="")
                else:
                    print("__ ", end="")
            print()
            if i == 10:
                break
            print("%d |" % i, end="")
            for j in range(1,10):
                if j==3 or j==6:
                    print("%s "%str(self.dic1[(i, j)])+ "\033[31m" + "|" + "\033[0m" , end="")
                else:
                    print("%s |" % str(self.dic1[(i, j)]), end="")
            print()
        print()

player1=Player1(dic1,tup1,num_type)

player1.table()
print("Set the puzzle.")
while True:
    solution=player1.Sudoku()
    if solution=="Start":
        player1.num_type="ans"
    if solution!="back" and solution!="Start":
        player1.table()
    if solution=="Solved" or solution=="Not solved" or solution=="Start":
        print("%s!!"%solution)
    if solution=="Solved":
        break
