import serial, time


def __main__():
	
	ser = serial.Serial('/dev/ttyACM1', 115200)
	file = open("data.txt", "w")
	piece = []
	while True :
		try:

			ser.name
			str1 = ser.read()
			# file.write(str)
			str2 = ser.read()
			# file.write(str)
			# str3 = ser.read()
			# # file.write(str)
			# str4 = ser.read()
			# print(str1)
			# print(str2)
			if(int(str1) > 8 or int(str1) < 1 or int(str2) > 8 or int(str2) < 1):
				continue
			else:
				str = str1 + ',' + str2
				if(str not in piece):
					piece.append(str)
					file.write(str)
					file.write('\n')
					print("write: "+str+"\n")
					# time.sleep(1)	
					file.flush() 	
					# file.close()

		except:
			pass


if __name__=="__main__":
    __main__()