import random
import sys
import math

def isValidArray(array):
	for e in array:
		if e > 0:
			return True
	return False


def generateArrays(min, max):

	n = [min]
	i = 0
	while n[i] * 2 < max:
		n.append(n[i] * 2)
		i = i + 1


	arrays = []
	for e in n:
		array = random.sample(range(-10*e, 10*e), e)
		while not isValidArray(array):
			array = random.sample(range(-1000, 1000), e)
		arrays.append(array)	
	return arrays