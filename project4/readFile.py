import sys
import dptsp

if(len(sys.argv)  < 2):
	print "Did not specify filename.\nExiting"
	exit(0)
	
filename = sys.argv[1].strip("\\")
filenameExt = filename[-4:]

if(filenameExt not in ".txt"):
	print "Invalid filetype.\nExiting."
	exit(0)
	
inputFile = open(filename, 'r')

#list of lists. Each sublist is [id, xCoord, yCoord]
fullMap = []

while True:
	values = inputFile.readline()
	if not values:
		break
	if values == [''] or values[0] == '\n':
		continue
	
	#now, parse file
	values = values.split()
	values = map(int, values)
	
	fullMap.append(values)

	
#call TSP func with fullMap


	