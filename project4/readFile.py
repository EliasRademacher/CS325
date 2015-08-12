import sys
import math
from greedyTSP import greedyTsp

def visitCityPath(dictionary, list):
	i = 0
	distance = 0
	while i < len(list)-1:
		if (list[i], list[i+1]) in dictionary:
			distance = distance + dictionary[(list[i], list[i+1])]
		else:
			distance = distance + dictionary[(list[i+1], list[i])]
		i += 1

	if (list[0], list[-1]) in dictionary:
		distance = distance + dictionary[(list[0], list[-1])]
	else:
		distance = distance + dictionary[(list[-1], list[0])]
	
	print distance

if(len(sys.argv)  < 2):
	filename = "test-input-1.txt"

else:
	filename = sys.argv[1].strip("\\")
	if(filename[-4:] != ".txt"):
		print "Invalid filetype.\nExiting."
		exit(0)
	
	
inputFile = open(filename, 'r')
listFile = open(sys.argv[2])

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

solnList = []	
for line in listFile:
	solnList.append(int(line))
solnList.pop(0)
	
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
#greedyTsp(lengthDictionary, n)
print solnList
print
visitCityPath(lengthDictionary, solnList)
	
		
	