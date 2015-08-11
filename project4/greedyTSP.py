import sys

def greedyTsp(dictionary, n):
	newDict = {}
	
	#(starting node, distance)
	#shortest = (-1, sys.maxint)
	# for i in range(0 : n):
		# results = findRoute(i, n, dictionary)
		# newDict[i] = results[0]
		
		# if(results[1] < shortest[1]):
			# shortest = (i, results[1])
			
	findRoute(0, n, dictionary)
	
	

def findRoute(start, n, dictionary):
	
	ids = nList(start, n)
	currentNode = start
	route = [(start, 0)]
	totalLen = 0
	count = 0
	
	while count < n-1:
		print "current node: " + str(currentNode)
		print "ids: " + str(ids)
		shortest = sys.maxint
		shortestNode = -1
		for id in ids:
			if((currentNode, id) in dictionary):
				length = dictionary[(currentNode, id)]
			else:
				length = dictionary[(id, currentNode)]
			
			print "node:" + str(id) + " length: " + str(length)
			
			if(length < shortest):
				shortest = length
				totalLen += shortest
				shortestNode = id
		
		print "picked node: " + str(shortestNode) + " at len: " + str(shortest) + "\n"
		currentNode = shortestNode
		route.append((currentNode, shortest))
		ids.remove(currentNode)
		count += 1

	#TODO: Add route back to start node	

	for r in route:
		print "id: " + str(r[0]) + ", distance: " + str(r[1])
	print "*****Total Length*****\n" + str(totalLen) + "\n*****Total Length*****"
	return route, totalLen
	


def nList(start, n):
	list = []
	for i in range(0, n):
		if(i != start):
			list.append(i)
	return list
	