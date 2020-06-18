
import time
import os
import pyperclip

# v1- basic working version:
# v2- copy current egg counts to clipboard

collectedTypes = ["kraken's ink","cuttle box","tentacle locker","cephalo pod","kraken's egg"]
collectedTypes = ["kraken's egg","cephalo pod","tentacle locker","cuttle box","kraken's ink"]

def main():

	# characters chat log file
	fileName = r'C:\Users\*****\AppData\Roaming\Three Rings Design\chat log\****_emerald_chat.log'

	fileHandle= open(fileName,'r')
	counter = KhCounter()
	counter.updateDisplay()

	if 1:
		for i in follow(fileHandle):
			line = i[0:-1]
			if "loaded".casefold() in line.casefold():
				counter.parse(i)

def follow(thefile):
	thefile.seek(0,2) # Go to the end of the file
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1) # Sleep briefly
			continue
		yield line


class KhCounter:

	def __init__(self):
		self.eggCount = {}

	def parse(self,textLine):
		lineWords = textLine.split(' ')
		textTime = lineWords[0]
		person = lineWords[1]

		for i, chestType in enumerate(collectedTypes):
			if chestType in textLine:
				self.add2count(person,i)

	def add2count(self, person, chestType):
		
		if person not in self.eggCount.keys():
			self.eggCount[person] = [0]*len(collectedTypes)

		self.eggCount[person][chestType] +=1
		self.updateDisplay()

	def updateDisplay(self):

		# clear display:
		os.system('cls')

		total = [0]*len(collectedTypes)

		playerList = list( self.eggCount.keys() )

		# get longest player name
		maxPlayerName = len(" Player ")
		for p in playerList:
			if len(p) > maxPlayerName:
				maxPlayerName = len(p)
		
		collectedTypeheaders = [ padStr(i, len(i)+2) for i in collectedTypes]
		collumnWidths = [maxPlayerName] + [len(i)+2 for i in collectedTypes]


		header=[ padStr("Player", maxPlayerName) ] + collectedTypeheaders
		headerStr = '|'.join(header)

		# generate header
		print( headerStr )
		for i in range(len(headerStr)):
			print('_',end='')
		print('')

		for p in self.eggCount.keys():
			print(padStr(p,collumnWidths[0]),end='|')
			for i,v in enumerate(self.eggCount[p]):
				total[i] += v
				print(padStr(str(v),collumnWidths[i+1]),end='|')
			print('')
		
		for i in range(len(headerStr)):
			print('_',end='')
		print('')

		print(padStr('Total',collumnWidths[0]),end='|')
		for i,v in enumerate(total):
			print(padStr(str(v),collumnWidths[i+1]),end='|')
		print('')

		self.loadOverallToClipBoard()

	def loadOverallToClipBoard(self):
		str4Clip = ""
		for p in self.eggCount.keys():
			str4Clip = str4Clip + p + ": ( Eggs:" + str(self.eggCount[p][0])

			if self.eggCount[p][1] >0:
				str4Clip = str4Clip + " Pods:" + str(self.eggCount[p][1])

			if self.eggCount[p][2] >0:
				str4Clip = str4Clip + " Lockers:" + str(self.eggCount[p][2])

			if self.eggCount[p][3] >0:
				str4Clip = str4Clip + " Boxes:" + str(self.eggCount[p][3])

			str4Clip = str4Clip + ") "
		
		pyperclip.copy(str4Clip)





def padStr( rawString, length):
	strLen = len(rawString)

	leftpad = (length-strLen)//2
	rightpad = length - strLen - leftpad

	leftpad = ' ' * leftpad
	rightpad = ' ' * rightpad
	return (leftpad + rawString + rightpad)




if __name__ == "__main__":
	main()