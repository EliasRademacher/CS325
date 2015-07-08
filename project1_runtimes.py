# Compares execution times of different implementations of the max
# subarray function

import maxSubArray
import timeit

REPEAT = 100
results = open("./MSS_Results.txt", "w")
input = open("./MSS_TestProblems.txt", "r")




results.write("Input\t\tAlgorithm 1\t\tAlgorithm 2\n")
results.write("     \t\truntime (seconds)\truntime (seconds)\n\n")

for n in input:
	stmt = 'maxSubArray.maxSubArray1(' + str(n) + ')'
	setup = "from __main__ import maxSubArray"
	results.write("\t\t" + "{:f}".format(timeit.timeit(stmt, setup, number=REPEAT)))
	
	stmt = 'maxSubArray.maxSubArray2(' + str(n) + ')'
	setup = "from __main__ import maxSubArray"
	results.write("\t\t" + "{:f}".format(timeit.timeit(stmt, setup, number=REPEAT)))
	results.write("\n")


results.close()
input.close()