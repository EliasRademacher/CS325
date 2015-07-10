import maxSubArray
import sys 

def testArrayFunctions(array, algorithms):
	results = []
	i = 0
	for algorithm in algorithms:
		results.append(algorithm(array))
		maxSum = results[i][0]
		subArray = results[i][1]
		print str(algorithm).split()[1]
		print "Maximum Sum: " + str(maxSum)
		print "Sub-array: " +  str(subArray) + "\n"
		
		if i > 0:
			assert(results[i] == results[i - 1])
		
		i = i + 1


testArrays = open(".\MSS_TestProblems.txt", 'r')
sys.stdout = open(".\MSS_Results.txt", "w")

algorithms = [maxSubArray.maxSubArray1, \
	maxSubArray.maxSubArray2, \
	maxSubArray.maxSubArray3, \
	maxSubArray.maxSubArray4]


for array in testArrays:
	if array[0] == '#' or array[0] == '\n':
		continue
	testArrayFunctions(eval(array), algorithms)
	print

testArrays.close()
