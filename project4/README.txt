**** README ****
This project is a solution to the Travelling Salesman Problem usingthe greedy 
'Nearest Neighbor' algorithm.

It takes in a file of the form:

	(int) (int) (int)
	(int) (int) (int)
	(int) (int) (int)
	(int) (int) (int)

where the first column is the cityId (must be in increasing order, from top to
bottom, beginning at zero. The second column is the 'x' cartesian coordinate, and the
third is the 'y' cartesian coordinate for the city in that row.

Running instructions:
	
	Files needed: (Must be within directory named: src)
	- city file (.txt)
	- settings.py
	- readFile.py
	- greedyTSP.py

	To run:
	type "python readFile.py [cityfile.txt]" without quotes.


NOTE:
 - This program is compatible with Windows and Linux systems.
 - Code must be kept in file called 'src'
 - The program will timeout after 5 minutes and produce the best solution that it
	has found, unless it hasn't found one. To prevent the timeout,
	give a third command line argument "nokill" 
