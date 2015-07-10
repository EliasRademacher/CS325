# Compares execution times of different implementations of the max
# subarray function

import maxSubArray
import timeit
import randomArray


MAX_ARRAY_LENGTH = 6000
MIN_ARRAY_LENGTH = 10
REPEAT = 1

algorithms = [maxSubArray.maxSubArray1, \
	maxSubArray.maxSubArray2, \
	maxSubArray.maxSubArray3, \
	maxSubArray.maxSubArray4]



arrays = randomArray.generateArrays(MIN_ARRAY_LENGTH, MAX_ARRAY_LENGTH)

results = open("./timingResults.txt", "w")

results.write("Runtimes for maximum sub-array algorithms (seconds)\n\n")
results.write("Array\t\tAlgorithm 1\t\tAlgorithm 2\t\tAlgorithm 3\t\tAlgorithm 4\n")
results.write("Length\n\n")

for array in arrays:
	results.write(str(len(array)))
	for algorithm in algorithms:
		stmt = 'maxSubArray.' + str(algorithm).split()[1] + '(' + str(array) + ')'
		setup = "from __main__ import maxSubArray"
		results.write("\t\t\t" + str(timeit.timeit(stmt, setup, number=REPEAT)))
	results.write("\n")

results.close()




