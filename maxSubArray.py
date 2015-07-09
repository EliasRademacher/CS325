#CS 325 Group Project 1
import sys
import math


def maxSubArray1(array):

	subArrayLength = 1
	maxSum = 0
	start = -1
	end = -1
	
	# Compare all subarrays in array.
	while subArrayLength <= len(array):
	
		# Vary starting index of subarray
		i = 0
		while i <= len(array) - subArrayLength:
			sum = 0
			
			# Calculate all sums of all subarrays of length subArrayLength
			for j in range(subArrayLength):
					sum = sum + array[j + i]
			if sum > maxSum:
				maxSum = sum
				start = i
				end = j + i
			i = i + 1
				
		subArrayLength = subArrayLength + 1

	return maxSum, array[start:end + 1]

	
		
	
def maxSubArray2(array):
	
	end = len(array)
	maxSum = 0
	start = 0
	
	# Adjusts the starting index of the sub-array
	for j in range(len(array) - 1):
		
		i = j
		tempSum = 0
		
		# Adds up elements starting with j
		# as long as this increases the sum.
		while i < len(array) - 1:
			tempSum = tempSum + array[i]
			if tempSum > maxSum:
				maxSum = tempSum
				start = j
				end = i					
			i = i + 1
	
	return maxSum, array[start:end + 1]
		
		


def subroutine(array, low, mid, high):
	maxLeft = mid
	maxRight = mid
	leftSum = -sys.maxint
	sum = 0 
	i = mid
	while i >= low:
		sum = sum + array[i]
		if sum > leftSum:
			leftSum = sum
			maxLeft  = i
		i = i - 1
		
	rightSum = -sys.maxint
	sum = 0
	j = mid + 1
	while j < high:
		sum = sum + array[j]
		if sum > rightSum:
			rightSum = sum
			maxRight = j
		j = j + 1
	return (leftSum + rightSum, maxLeft, maxRight)
	
		
	
def divideAndConquer(array, low, high):
	if high == low:
		return (array[low - 1], low, high)
	else:
		mid = int(math.floor((low+high)/2))
		(leftSum, leftLow, leftHigh) = divideAndConquer(array, low, mid)
		(rightSum, rightLow, rightHigh) = divideAndConquer(array, mid+1, high)
		(crossSum, crossLow, crossHigh) = subroutine(array, low, mid, high)
	
		if leftSum >= rightSum and leftSum >= crossSum:
			return 	(leftSum, leftLow, leftHigh)
		elif rightSum >= leftSum and rightSum >= crossSum:
			return (rightSum, rightLow, rightHigh) 
		else:
			return (crossSum, crossLow, crossHigh) 

def maxSubArray3(array):
	low = 0
	high = len(array)
	(maxSum, start, end) = divideAndConquer(array, low, high)
	return maxSum, array[start:end + 1]



def maxSubArray4(array):
	n = len(array)
	maxSum = -sys.maxint
	endingHereSum = -sys.maxint
	
	i = 0
	while i < n:
		endingHereHigh = i
		if endingHereSum > 0:
			endingHereSum = endingHereSum + array[i]
		else:
			endingHereLow = i
			endingHereSum = array[i]
		if endingHereSum > maxSum:
			maxSum = endingHereSum
			low = endingHereLow 
			high = endingHereHigh
		
		i = i + 1
	
	return (maxSum, array[low:high + 1])
