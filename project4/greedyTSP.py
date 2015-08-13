import sys
import math


def greedyTsp(cities, numCities, q):
	minCost = sys.maxint
	cheapesRoute = []
	for startingCity in range(numCities):
		print str(startingCity)
		results = findRoute(startingCity, numCities, cities, minCost)	
		if(results != None):
			totalCost = results[1]
			if(totalCost < minCost):
		    		minCost = totalCost
				if(not q.empty()):
					q.get()	
					q.get()			
				q.put(results[0])
				q.put(minCost)
	return
##END 'def greedyTsp()'



def findRoute(startCity, numCities, cities, minCost):
	
	citiesToCheck = nList(startCity, numCities)
	currentCity = startCity
	route = [(startCity, 0)]
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
		route.append((currentCity, shortest))
		citiesToCheck.remove(currentCity)
		count += 1

	##Route back to start node	
	endLen = getLength(cities, startCity, currentCity)
	totalLen += endLen
	route.append((startCity, endLen))
		
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

	
