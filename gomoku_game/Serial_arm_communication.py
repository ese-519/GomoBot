import serial
import time

class MoveGomoBot(object):
	"""docstring for MoveGomoBot"""
	def __init__(self):
		super(MoveGomoBot, self).__init__()
		# self.arg = arg
		self.ser = serial.Serial(
			port='/dev/ttyUSB4',
			baudrate=115200,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS
			# timeout=0.050	
		)
		if self.ser.isOpen():
			self.ser.close()
		self.ser.open()
		self.ser.isOpen()
		time.sleep(1)
		print(self.ser.readline())
		while self.ser.inWaiting() > 0:
			print(self.ser.readline())

		#Some Hardcoded coordinates
		self.pieceLocation = [200,-200]
		self.lowerLeftCoor = [187,95] #0,0
		self.upperRighCoor = [380,-100] #8,8
		self.preCoor = (0,0)

	def calculateCoor(self,board_x,board_y):
		real_x = (self.upperRighCoor[0]-self.lowerLeftCoor[0]) / 8 * board_x + self.lowerLeftCoor[0]
		real_y = (self.upperRighCoor[1]-self.lowerLeftCoor[1]) / 8 * board_y + self.lowerLeftCoor[1]
		return real_x,real_y

	def readCoor(self):
		self.cam_list=[]
		time.sleep(2)
		f = open("arm.txt","r")
		content = f.readline()
		print(content)
		coordinates = content.split(',')
		if(self.preCoor == coordinates):
			coordinates = (0, 0)
		else:
			self.preCoor = coordinates
		f.close()
		print(int(coordinates[0]), int(coordinates[1]))
		return (int(coordinates[0]), int(coordinates[1]))


	def moveToBoard(self,board_x,board_y):
		#move the robot arm to x,y coordinate in board frame
		real_x, real_y = self.calculateCoor(board_x,board_y) 
		self.moveToPiece(1)
		self.moveToPiece(0)
		self.suckIt(1)
		self.waitForSec(1)
		self.moveToPiece(1)
		self.moveToCoor(real_x,real_y,0)
		self.moveToCoor(real_x,real_y,-50)
		self.suckIt(0)
		self.waitForSec(2.5)
		self.moveToCoor(real_x,real_y,0)
		self.moveToPiece(1)

	def moveToPiece(self,h):
		if h==1:
			self.moveToCoor(self.pieceLocation[0],self.pieceLocation[1],0)
		else:
			self.moveToCoor(self.pieceLocation[0],self.pieceLocation[1],-55)

	def waitForSec(self,sec):
		temp_input = 'G4 '+'P'+str(sec*1000)
		print(temp_input)
		self.ser.write(temp_input+'\r\n')

	def moveToCoor(self,x,y,z):
		#move the robot arm to x,y,z coordinate in world frame
		temp_input = 'G0 '+'X'+str(x)+' Y'+str(y)+' Z'+str(z)
		print(temp_input)
		self.ser.write(temp_input+'\r\n')

	def suckIt(self,x):
		#Suck it up
		if x==1:
			temp_input = 'M1000'
			self.ser.write(temp_input+'\r\n')
		else:
			temp_input = 'M1002'
			self.ser.write(temp_input+'\r\n')				

	def inputToMoveCoor(self):
		while 1 :
			# get keyboard input
			input = raw_input(">> ")
				# Python 3 users
				# input = input(">> ")
			if input == 'exit':
				self.ser.close()
				exit()
			else:
				# send the character to the device
				# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
				self.ser.write(input + '\r\n')
				print(input + '\n')
				out = ''
				# let's wait one second before reading output (let's give device time to answer)
				time.sleep(0.5)
				while self.ser.inWaiting() > 0:
					out += self.ser.read(1)
					
				if out != '':
					print ">>" + out

	def inputToMoveBoard(self):
		while 1 :
			# get keyboard input
			input = raw_input(">> ")
				# Python 3 users
				# input = input(">> ")
			if input == 'exit':
				self.ser.close()
				exit()
			else:
				# send the character to the device
				# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
				self.ser.write(input + '\r\n')
				print(input + '\n')
				out = ''
				# let's wait one second before reading output (let's give device time to answer)
				time.sleep(0.5)
				while self.ser.inWaiting() > 0:
					out += self.ser.read(1)
					
				if out != '':
					print ">>" + out

	def demoMove(self):
		raw_input("Please enter to continue")
		self.moveToCoor(0,200,0)
		raw_input("Please enter to continue")
		self.moveToCoor(0,200,-60)
		raw_input("Please enter to continue")
		self.suckIt(1)
		raw_input("Please enter to continue")
		self.moveToCoor(0,200,0)
		raw_input("Please enter to continue")
		self.moveToCoor(300,0,0)
		raw_input("Please enter to continue")
		self.moveToCoor(300,0,-55)
		raw_input("Please enter to continue")
		self.suckIt(0)
		raw_input("Please enter to continue")

	def demoMoveBoard(self):
		for i in range(3,6):
			for j in range(3,6):
				raw_input("Please enter to continue")
				print(i,j)
				self.moveToBoard(i,j)

	def closePort(self):
		self.ser.close()

if __name__ == '__main__':
	M = MoveGomoBot()
	raw_input("Please enter to continue")
	print("main")
	# M.demoMove()
	# M.demoMoveBoard()
	while(1):
		coordinates = M.readCoor()
		if(coordinates == (0,0)):
			print("pass")
			continue
		else:	
			M.moveToBoard(coordinates[0], coordinates[1])
	M.closePort()





