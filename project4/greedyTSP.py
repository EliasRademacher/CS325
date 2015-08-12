import sys

def greedyTsp(dictionary, n):
	newDict = {}
	shortestRoute = None
	
	#(starting node, distance)
	shortest = (-1, sys.maxint)
	for i in range(0, n):
		results = findRoute(i, n, dictionary)
		newDict[i] = results[0]
		
		if(results[1] < shortest[1]):
			shortest = (i, results[1])
			shortestRoute = results[0]
	
	print "\nSHORTEST ROUTE: " + str(shortest[1]) 
	for route in shortestRoute:
		print "id: " + str(route[0]) + ", distance: " + str(route[1])
	

def findRoute(start, n, dictionary):
	
	citiesToCheck = nList(start, n)
	currentNode = start
	route = [(start, 0)]
	totalLen = 0
	count = 0
	
	while count < n-1:
#		print "current node: " + str(currentNode)
#		print "citiesToCheck: " + str(citiesToCheck)
		shortest = sys.maxint
		shortestNode = -1
		for id in citiesToCheck:
			if((currentNode, id) in dictionary):
				length = dictionary[(currentNode, id)]
			else:
				length = dictionary[(id, currentNode)]
			
#			print "node:" + str(id) + " length: " + str(length)
			
			if(length < shortest):
				shortest = length
				totalLen += shortest
				shortestNode = id
		
#		print "picked node: " + str(shortestNode) + " at len: " + str(shortest) + "\n"
		currentNode = shortestNode
		route.append((currentNode, shortest))
		citiesToCheck.remove(currentNode)
		count += 1

	#Route back to start node	
	if(start, shortestNode) in dictionary:
		endLen = dictionary[(start, shortestNode)]
		route.append((start, endLen))
		totalLen += endLen
	else:
		endLen = dictionary[(shortestNode, start)]
		route.append((start, endLen))
		totalLen += endLen
		
	for r in route:
		print "City Id: " + str(r[0]) + ", distance: " + str(r[1])
	print "*****Total Length*****\n" + str(totalLen) + "\n*****Total Length*****"
	return route, totalLen
	


def nList(start, n):
	list = []
	for i in range(0, n):
		if(i != start):
			list.append(i)
	return list
	