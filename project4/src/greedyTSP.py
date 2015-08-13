import sys
import math
import multiprocessing
import settings
from settings import *


def singleDataTransfer(minCost, route, q):
	out = open(TEMP1, "w")
	out.write(str(minCost) + "\n")
	print "minCost: " + str(minCost)
	for e in route:
		out.write(str(e) + "\n")
	q.put(TEMP1)
	out.close
	
	
def multiDataTransfer(alternator, minCost, route, q):
	out = None
	filename = TEMP1
	if(alternator == False):
		filename = TEMP2
		
	out = open(filename, "w")
	out.write(str(minCost) + "\n")
	print "minCost: " + str(minCost)
	for e in route:
		print e
		out.write(str(e) + "\n")
	
	q.put(filename)
	out.close
	return False if alternator else True
	
	

def greedyTsp(cities, numCities, q):
	minCost = sys.maxint
	shortestRoute = []
	alternator = True
	for startingCity in range(numCities):
		print "startingCity: " + str(startingCity)
		results = findRoute(startingCity, numCities, cities, minCost)	
		if(results != None):
			totalCost = results[1]
			print "total cost: " + str(totalCost)
			if(totalCost < minCost):
				minCost = totalCost
				shortestRoute = results[0]
				
				if(numCities > settings.MAX_TIMED_CITIES):
					##Write data to file to be accessed by parent.
					##If alternator is True, write to TEMP1, else to TEMP2 
					alternator = multiDataTransfer(alternator, minCost, shortestRoute, q)
	
	##If there is time, just pass data now
	singleDataTransfer(minCost, shortestRoute, q)
##END 'def greedyTsp()'



def findRoute(startCity, numCities, cities, minCost):
	
	citiesToCheck = nList(startCity, numCities)
	currentCity = startCity
	route = [(startCity)]
	totalLen = 0
	count = 0
	
	while count < numCities - 1:
		shortest = sys.maxint
		closestCityId = -1
		for id in citiesToCheck:
			length = getLength(cities, id, currentCity)
			if(length < shortest):
				shortest = length		
				closestCityId = id
		
		totalLen += shortest

		#prematurely kill if cost is too high
		if(totalLen > minCost):
			return None
		
		currentCity = closestCityId
		route.append((currentCity))
		citiesToCheck.remove(currentCity)
		count += 1

	##Route back to start node	
	endLen = getLength(cities, startCity, currentCity)
	totalLen += endLen
	route.append((startCity))
		
	return route, totalLen
	


def nList(start, n):
	list = []
	for i in range(0, n):
		if(i != start):
			list.append(i)
	return list

	
def getLength(cities, city1, city2):
	city1x = cities[city1][1]
	city1y = cities[city1][2]
	city2x = cities[city2][1]
	city2y = cities[city2][2]
	return int(round(math.sqrt(((city1x - city2x)**2) + ((city1y - city2y)**2))))

	
