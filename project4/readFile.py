import sys
import math
from greedyTSP import greedyTsp

if(len(sys.argv)  < 2):
	filename = "test-input-1.txt"

else:
	filename = sys.argv[1].strip("\\")
	if(filename[-4:] != ".txt"):
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

#number of 'cities'
n = len(fullMap)
	
#create distances dictionary
lengthDictionary = {}
for a in fullMap:
	for b in fullMap:
		#eliminate duplicate values
		if(a[0] < b[0]):
			lengthDictionary[(a[0], b[0])] = int(round(math.sqrt(((a[1] - b[1])**2) + ((a[2] - b[2])**2))))

#****FOR TESTING
for key in lengthDictionary.keys():
	print "key:", str(key), "val:", lengthDictionary[key]
print 
#****FOR TESTING


#call TSP func with dictionary
greedyTsp(lengthDictionary, n)

	