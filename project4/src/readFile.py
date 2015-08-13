import sys
import math
from greedyTSP import greedyTsp
import time
import Queue
import multiprocessing
import os
from settings import *


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
	print "\n*** No File entered. Exiting ***\n"
	exit(0)

else:
	filename = sys.argv[1].strip("\\")
	if(filename[-4:] != ".txt"):
		print "\n*** Invalid filetype.\nExiting ***\n"
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

inputFile.close()

##number of 'cities'
n = len(fullMap)

if __name__ == '__main__':
	q = multiprocessing.Queue(-1)
    	p = multiprocessing.Process(target=greedyTsp, 
		name='greedyTsp', args=(fullMap, n, q))
	p.start()

	while(p.is_alive()) and (time.time() < startTime + 295):
	    	continue	
	
	p.terminate()
	print "\nTerminated...\n"
	
	if(q.empty()):
		print "Queue empty, blocking"
	
	tempResults = None
	while(not q.empty()):
		print "getting tempResults"
		tempResults = q.get(True, 5)

	p.join()
	print "\nJoined...\n"
	
	#rename temp to output file 
	outFile = filename + ".tour"
	if(os.path.isfile(outFile)):
		os.remove(outFile)
		
	print "tempResults: " + tempResults
	os.rename(tempResults, outFile)
	
	print "done"
	
	if(os.path.isfile(TEMP1)):
		os.remove(TEMP1)
	if(os.path.isfile(TEMP2)):
		os.remove(TEMP2)
	