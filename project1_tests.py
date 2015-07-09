import maxSubArray


	
def testArrayFunctions(array, algorithms):
	results = []
	i = 0
	for algorithm in algorithms:
		results.append(algorithm(array))
		print "Algorithm ", i + 1
		print "Maximum Sum: " + str(results[i][0])
		print "Sub-array: " +  str(results[i][1]) + "\n"
			
		assert(results[i][0] == 187)
		assert(results[i][1] == [59, 26, -53, 58, 97])

		
		
		i = i + 1



array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

algorithms = [maxSubArray.maxSubArray1, \
	maxSubArray.maxSubArray2, \
	maxSubArray.maxSubArray3, \
	maxSubArray.maxSubArray4]

		
testArrayFunctions(array, algorithms)