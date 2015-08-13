import sys
import math
from greedyTSP import greedyTsp
import time
import Queue
import multiprocessing

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
##END FUNC

startTime = time.time()
if(len(sys.argv)  < 2):
	filename = "test-input-1.txt"

else:
	filename = sys.argv[1].strip("\\")
	if(filename[-4:] != ".txt"):
		print "Invalid filetype.\nExiting."
		exit(0)
	
	
inputFile = open(filename, 'r')

##list of lists. Each sublist is [id, xCoord, yCoord]
fullMap = []

while True:
	values = inputFile.readline()
	if not values:
		break
	if values == [''] or values[0] == '\n':
		continue
	
	##now, parse file
	values = values.split()
	values = map(int, values)
	
	fullMap.append(values)
	
##number of 'cities'
n = len(fullMap)

if __name__ == '__main__':
	q = multiprocessing.Queue()
    	p = multiprocessing.Process(target=greedyTsp, 
		name='greedyTsp', args=(fullMap, n, q))
	p.start()

	while(p.is_alive()) and (time.time() < startTime + 295):
	    	continue	
	p.terminate()
	p.join()
	print "terminated and joined"
	
	cheapestRoute = q.get()
	print "got cheapest route"
	minCost = q.get()

	outputFile = open(filename + '.tour', 'w')
	
	print(str(minCost))
	print "Cost: " + str(minCost)

	outputFile.write(str(minCost) + "\n")
	
	print "wrote p1"
	
	for edge in cheapestRoute:
		outputFile.write(str(edge[0]) + "\n")
		print str(edge[0])
	
	print "wrote p2"
	outputFile.close()
			
##****FOR TESTING
# for key in lengthDictionary.keys():
	# print "key:", str(key), "val:", lengthDictionary[key]
# print 

#To test against sol'n files
# listFile = open(sys.argv[2]) 
# solnList = []	
# for line in listFile:
	# solnList.append(int(line))
# solnList.pop(0)
# print solnList
# print
# visitCityPath(lengthDictionary, solnList)
##****FOR TESTING




	
		
	
