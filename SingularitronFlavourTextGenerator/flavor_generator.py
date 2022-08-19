from libs import pyFlavText
import time

def MaximumFlava():
	# define parameters
	num1 = int(9223372036854775807)
	num2 = 0
	timeBetw = float(1)
	# just empty space, don't worry about it
	print("")
	# loop to produce output desired no. of times
	while num2 < num1:
		output = pyFlavText.testingLOL()
		# strLenny = len(output)
		# for debugging purposes
		# print(strLenny) # ( ͡° ͜ʖ ͡°)
		num2+=1
		time.sleep(timeBetw)

MaximumFlava()
