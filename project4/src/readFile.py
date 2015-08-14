import sys
import math
from greedyTSP import greedyTsp, getLength
import time
import Queue
import multiprocessing
import os
from settings import *


def visitCityPath(fullMap, solnList):
	totalLen = solnList[0]
	calcLen = 0
	i = 1
	while i < (len(solnList) - 1):
		edgeCost = getLength(fullMap, solnList[i], solnList[i+1])
		calcLen +=  edgeCost
		i += 1 
	calcLen += getLength(fullMap, solnList[1], solnList[-1])
	
	if calcLen != totalLen:
		print "\nERROR BAD LENGTHS\n"
		print "actual: " + str(calcLen)
		print "found: " + str(totalLen)
	else:
		print "checksum succeeded!"
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

kill = True
if(len(sys.argv) == 3):
	if sys.argv[2] == "nokill":
		print "NOKILL RECEIVED"
		kill = False
	
	
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

	if(kill):
		while(p.is_alive() and (time.time() < startTime + TIMEOUT)):
			continue	
	else:
		while(p.is_alive()):
			continue
	
	p.terminate()
	print "\nTerminated...\n"
	endTime = time.time() - startTime
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
	
	if(tempResults == None):
		print "\nNo solution found.\n"
		cleanup()
		exit(0)
		
	os.rename(tempResults, outFile)
	
	print "done in " + str(endTime) + " seconds"
	timeFile = open(filename + ".time", "w")
	timeFile.write("Time elapsed: " + str(endTime))
	close(timeFile)
	
	print "\nTESTING SOLN\n"
	solnList = []
	solnFile = open(outFile, "r") 
	for line in solnFile:
		solnList.append(int(line))
	visitCityPath(fullMap, solnList)
	
	cleanup()
	