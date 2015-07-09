import random
import sys

def isValidArray(array):
	for e in array:
		if e > 0:
			return True
	return False


def generateArray(n):
	arrays = []
	for e in n:
		array = random.sample(range(-10*e, 10*e), e)
		while not isValidArray(array):
			array = random.sample(range(-1000, 1000), e)
		arrays.append(array)	
	return arrays

	
	
n = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]		
f = open("./randomArrays.txt", "w")
arrays = generateArray(n)
count = 0
for a in arrays:
	print "array: " + str(count)
	print a
	f.write(str(a))
	f.write("\n")
	count = count + 1
f.close()