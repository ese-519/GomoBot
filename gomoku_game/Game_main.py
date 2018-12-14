import Game_board as b
import ast
import Game_evaluation_functions as ef
import Queue as q
import time

def y_axis(y):
    return y - 1

def x_axis(x):
    return 9 - x

def arm_coordinate(x,y):
    f = open("arm.txt", "w")
    print("file open")
    while True :
        try:
            # str1 = str(x) + ',' + str(y)
            print(x)
            print(y)
            str1 = str(y-1) + ',' + str(9-x)
            print("write: "+str1+"\n")
            f.write(str1)
            f.write('\n')
            f.flush() 
            break
        except:
            pass
    f.close()


class Gomoku:




    def __init__(self):
        self.white_list = []
        self.black_list = []
        self.cam_list = []
        self.playerInput = []

    def trans(self,(x,y)):
        return [x,y]

    def readFile(self):
        self.cam_list=[]
        f = open("data.txt","r")
        contents = f.readlines()
        for content in contents:
            coordinates = content.rstrip().split(',')
            self.cam_list.append([int(coordinates[0]),int(coordinates[1])])
        f.close()
        print(self.cam_list)

    def checkNewMove(self):
        checker = 0

        for elem in self.cam_list:
            if (elem not in self.white_list and elem not in self.black_list):
                checker+=1
                self.playerInput = elem

        if checker>1:
            print("More than one plays detected!!!")
            return False

        elif checker==1:
            print("Player moves at:", self.playerInput)
            return True

        else:
            print("No new plays detected")
            return False

    def playerNewMove(self,board):
        self.readFile()
        while not self.checkNewMove():
        	try:
	            self.readFile()
	            time.sleep(0.5)
	    	except KeyboardInterrupt:
	    		self.playerInput = self.enterPosition(board)
	    		self.cam_list.append([int(self.playerInput[0]),int(self.playerInput[1])])
        return self.playerInput


    def enterPosition(self,board):
        while True:
            while True:
                try:    
                    move = ast.literal_eval(raw_input("Please enter your move in format '(x,y)': "))
                    break
                except(ValueError,SyntaxError,TypeError):
                    print("error")
                    continue
            piece = self.trans(move)
            if(board._isValidMove((piece[0],piece[1]))):
                print(piece[0])
                break
            else:
                print("enter valid position")
                continue
        print("Black moved {0}".format(move))
        return piece


    def gomoku(self):
        board = b.Board()

        board.printBoard()

        tlimit = 2;
        print("player 1 moves first")
        piece = self.playerNewMove(board)
        # board._isBlack = True
        board.updateBoard((y_axis(piece[0]),x_axis(piece[1])))
        self.black_list.append([piece[0], piece[1]])

        print("GomoBot moves")
        # board._isBlack = False
        move = ef.secondmove(board, piece[0], piece[1])
        piece = self.trans(move)
        board.updateBoard((y_axis(piece[0]),x_axis(piece[1])))
        arm_coordinate(piece[0], piece[1])
        self.white_list.append([piece[0],piece[1]])

        while not board.win:

            print("Player moves")
            # raw_input('Press enter to continue: ')
            # piece = self.enterPosition(board)
            raw_input("Please enter to continue")
            piece = self.playerNewMove(board)
            # board._isBlack = True
            board.updateBoard((y_axis(piece[0]),x_axis(piece[1])))
            self.black_list.append([piece[0],piece[1]])

            if(board.win):
                break

            print("GomoBot moves")
            move = ef.nextMove(board,tlimit,3)
            board.updateBoard(move)
            self.white_list.append([move[0]+1,10 - move[1] - 1])
            arm_coordinate(move[0]+1, 10 - move[1] - 1)
            print("Black:", self.black_list)
            print("White:", self.white_list)

        print("GAME OVER")

if __name__=="__main__":
    G = Gomoku()
    # G.readFile()
    G.gomoku()



