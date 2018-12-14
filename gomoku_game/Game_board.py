import copy
class Board:

    def __init__(self):

        self.size = 9
        self.white = []
        self.black = []
        self.win = False
        self.board = [['.' for x in range(self.size)] for y in range(self.size)]
        self.winLog = "Win!"
        self.c = 'x'
        self._isBlack = True

    def _inBoard(self,(x,y)):

        return x>=0 and x<self.size and y>=0 and y<self.size

    def _isValidMove(self,(x,y)):

        return self._inBoard((x,y)) and self.board[x][y]=='.'

    def turn(self):
        
        return color(len(self.black)==len(self.white))

    def __getitem__(self,num): return self.board[num]

    def __len__(self): return 5

    def printBoard(self):
        for i in range(self.size):
            print (10 - i%10 - 1),
        print(" ")
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j]),
            print (i + 1),
            print (" ")

    def updateBoard(self,(x,y)):
        if(self._isBlack):
            self.c = 'x'
        else:
            self.c = 'o'

        if self._isBlack:
            if self._isValidMove((x,y)):
                self.black.append([x,y])
                self.board[x][y] = 'x'
            else:
                print("Error input, please enter a valid coordinate")

        else:
            if self._isValidMove((x,y)):
                self.white.append([x,y])
                self.board[x][y] = 'o'
            else:
                print("Error input, please enter a valid coordinate")

        self.printBoard()

        if self.checkWin(x,y):
            if self._isBlack: 
                print("Black") 
            else: 
                print("White")
            print(self.winLog)
            self.win = True
        self._isBlack = not self._isBlack


    def checkWin(self,x,y):
        if (self._checkH(x,y) or self._checkV(x,y) or self._checkL(x,y) or self._checkR(x,y)):
            return True
        else: 
            return False

    def _checkH(self,x,y):
        temp_count = 1
        tempx = x
        tempy = y
        for i in range(4):
            tempy += 1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break

        tempy = y
        for i in range(4):
            tempy-=1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1                  
            else:
                break

        if temp_count>4: 
            return True
        else:
            return False 

    def _checkV(self,x,y):
        temp_count = 1
        tempx = x
        tempy = y
        for i in range(4):
            tempx += 1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break
        tempx = x
        for i in range(4):
            tempx-=1            
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break

        if temp_count>4: 
            return True
        else:
            return False 

    def _checkL(self,x,y):
        temp_count = 1
        tempx = x
        tempy = y
        for i in range(4):
            tempx += 1
            tempy += 1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break
        tempx = x
        tempy = y
        for i in range(4):
            tempx-=1
            tempy-=1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break

        if temp_count>4: 
            return True
        else:
            return False            

    def _checkR(self,x,y):
        temp_count = 1
        tempx = x
        tempy = y
        for i in range(4):
            tempx += 1
            tempy -= 1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break
        tempx = x
        tempy = y
        for i in range(4):
            tempx-=1
            tempy+=1
            if (self._inBoard((tempx,tempy)) and self.board[tempx][tempy] == self.c):
                temp_count +=1
            else:
                break

        if temp_count>4: 
            return True
        else:
            return False            

    def move(self,(y,x)):
        """
        (y,x) : (int,int)
        return: board object

        Takes a coordinate, and returns a board object in which
        that move has been executed.  If self.win is True (the 
        board that move() is being executed on has already been
        won), then the move/piece-placement is not executed, and
        a copy of self is returned instead.
        If the coordinate entered is invalid (self._valid_move((y,x))==False)
        then the game is over, and win statement is set to explain that
        the opposite player wins by default
        """
        turn = self.turn()
        other = copy.deepcopy(self)
        if self.win:
            #print("The Game Is Already Over")attack
            return other
        if not other._isValidMove((y,x)):
            turn.swap()
            other.winstatement = "Invalid Move ({1},{2}) Played: {0} Wins by Default\n".format(str(turn),y,x)
            other.win = True
            return other
        
        other.board[y][x] = turn.symbol
        other.black.append((y,x)) if turn.isBlack else other.white.append((y,x))
        other.checkWin(x,y)
        return other

class color:
    """
    A simple color class.
    Initializes with a bool argument:
    Arbitrarily, True->color is black
                 False->color is white
    """
    def __init__(self, isBlack):
        if isBlack:
            self.isBlack = True
            self.color = "BLACK"
            self.symbol = "x"
        else:
            self.isBlack = False
            self.color = "WHITE"
            self.symbol = "o"

    def __eq__(self, other):
        return type(self)==type(other) and \
           self.color==other.color

    def __ne__(self,other): return not (self == other)

    def __str__(self): return self.color

    def __repr__(self): return str(self)

    def swap(self): #swaps a color object from Black->White or reverse
        self.__init__(not self.isBlack)

    def getNot(self): #returns a color object != self
        return color(not self.isBlack)          