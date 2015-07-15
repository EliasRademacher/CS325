import sys

def slowChange(value, denominations):
	coins = [0] * len(denominations)  #initialize to all zeros
	
	#base case
	if value in denominations:
		coins[denominations.index(value)] = coins[denominations.index(value)] + 1
		return coins
	
	#check all combinations of value
	for i in range(1, value):
		coins1 = slowChange(i, denominations)
		coins2 = slowChange((value - i), denominations)
		
		#store minimum number of coins (force first time)
		if ((sum(coins1) + sum(coins2)) < sum(coins)) or (i == 1):
			coins = [sum(x) for x in zip(coins1, coins2)]
			
	return coins
	
	
print slowChange(25, [1, 2, 4, 8])