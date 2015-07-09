import maxSubArray


array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]



algorithms = [maxSubArray.maxSubArray1, \
	maxSubArray.maxSubArray2, \
	maxSubArray.maxSubArray3]

i = 1	
for algorithm in algorithms:
	(maxSum, subArray) = algorithm(array)
	print "Algorithm ", i
	print "Maximum Sum: " + str(maxSum)
	print "Sub-array: " +  str(subArray) + "\n"
		
	assert(maxSum == 187)
	assert(subArray == [59, 26, -53, 58, 97])

	
	
	i = i + 1
