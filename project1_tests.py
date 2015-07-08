import maxSubArray


array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]


# assert(maxSubArray.maxSubArray1(array)[0] == 187)
# assert(maxSubArray.maxSubArray1(array)[1] == [59, 26, -53, 58, 97])

# assert(maxSubArray.maxSubArray2(array)[0] == 187)
# assert(maxSubArray.maxSubArray2(array)[1] == [59, 26, -53, 58, 97])

# assert(maxSubArray.maxSubArray3(array)[0] == 187)
# assert(maxSubArray.maxSubArray3(array)[1] == [59, 26, -53, 58, 97])

# assert(maxSubArray.maxSubArray2(array) == maxSubArray.maxSubArray1(array))
# assert(maxSubArray.maxSubArray3(array) == maxSubArray.maxSubArray1(array))

algorithms = [maxSubArray.maxSubArray1, \
	maxSubArray.maxSubArray2]

i = 0	
for algorithm in algorithms:
	(maxSum, subArray) = algorithm(array)
	print "Algorithm ", i
	print "Maximum Sum: " + str(maxSum)
	print "Sub-array: " +  str(subArray)
	
	i = i + 1
