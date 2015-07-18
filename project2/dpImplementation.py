def changedp(value, denominations, memoizedVals):
	coins = [0] * len(denominations)  #initialize to all zeros
	
	#base case
	if value in denominations:
		coins[denominations.index(value)] = coins[denominations.index(value)] + 1
		memoizedVals[value] = coins
		return coins	
	
	#check all combinations of value
	for i in range(1, value):
		coins1 = 0 
		coins2 = 0
		
		if (memoizedVals[i] == False):	
			coins1 = changedp(i, denominations, memoizedVals)
		else: 
			coins1 = memoizedVals[i]
			
		if (memoizedVals[value - i] == False):	
			coins2 = changedp(value - i, denominations, memoizedVals)
		else: 
			coins2 = memoizedVals[value - i]
		
			
		#store minimum number of coins (force first time)
		if ((sum(coins1) + sum(coins2)) < sum(coins)) or (i == 1):
			coins = [sum(x) for x in zip(coins1, coins2)]
			memoizedVals[value] = coins

	return coins
	
	
def wrapDP(value, denominations):
	memoizedVals = [False] * (value+1)
	return changedp(value, denominations, memoizedVals)