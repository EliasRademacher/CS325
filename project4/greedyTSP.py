import sys

def greedyTsp(dictionary, numCities):
	cheapestRoute = []
	minCost = sys.maxint
	
	for startingCity in range(numCities):
		results = findRoute(startingCity, numCities, dictionary)
		
		
		totalCost = results[1]
		
		if(totalCost < minCost):
			minCost = totalCost
			cheapestRoute = results[0]
	
	print "\nSHORTEST ROUTE: " + str(minCost) 
	for route in cheapestRoute:
		print "id: " + str(route[0]) + ", distance: " + str(route[1])
	

def findRoute(startCity, numCities, dictionary):
	
	citiesToCheck = nList(startCity, numCities)
	currentCity = startCity
	route = [(startCity, 0)]
	totalLen = 0
	count = 0
	
	while count < numCities - 1:
#		print "current node: " + str(currentCity)
#		print "citiesToCheck: " + str(citiesToCheck)
		shortest = sys.maxint
		closestCityId = -1
		for id in citiesToCheck:
			if((currentCity, id) in dictionary):
				length = dictionary[(currentCity, id)]
			else:
				length = dictionary[(id, currentCity)]
			
#			print "node:" + str(id) + " length: " + str(length)
			
			if(length < shortest):
				shortest = length
				totalLen += shortest
				closestCityId = id
		
#		print "picked node: " + str(closestCityId) + " at len: " + str(shortest) + "\n"
		currentCity = closestCityId
		route.append((currentCity, shortest))
		citiesToCheck.remove(currentCity)
		count += 1

	#Route back to start node	
	if(start, closestCityId) in dictionary:
		endLen = dictionary[(start, closestCityId)]
		route.append((start, endLen))
		totalLen += endLen
	else:
		endLen = dictionary[(closestCityId, start)]
		route.append((start, endLen))
		totalLen += endLen
		
	# for r in route:
		# print "City Id: " + str(r[0]) + ", distance: " + str(r[1])
	# print "*****Total Length*****\n" + str(totalLen) + "\n*****Total Length*****"
	return route, totalLen
	


def nList(start, n):
	list = []
	for i in range(0, n):
		if(i != start):
			list.append(i)
	return list
	