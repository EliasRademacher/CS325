import math, sys

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
	while j <= high:
		sum = sum + array[j]
		if sum > rightSum:
			rightSum = sum
			maxRight = j
		j = j + 1
	return (leftSum + rightSum, maxLeft, maxRight)
	
		
	
def divideAndConquer(array, low, high):
	if high == low:
		return (array[low], low, high)
	else:
		mid = int((low+high)/2)
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
	high = len(array) - 1
	(maxSum, start, end) = divideAndConquer(array, low, high)
	print maxSum
	return maxSum, array[start:end + 1]

array = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
maxSubArray3(array)