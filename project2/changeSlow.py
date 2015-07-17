# Algorithm 1 for Project 2
# CS 325, spring 2015

import sys

def changeSlow (v, c, a, level):
	
	coinSum = 0
	for value, numCoins in zip(v, c):
		coinSum = coinSum + (value * numCoins)
	
	if coinSum == a:
		return c
		
	
	i = 0
	while i < len(v):
		for j in range(level):
			sys.stdout.write(" ")
		sys.stdout.write(str(v[i]) + "  " + str(a) + "  " + str(c))
		print
		
		if v[i] == a:
			c[i] = c[i] + 1
			print "Amount equals a coin we have: ", a
			return c 
		i = i + 1

	i = 1
	minCoins = [sys.maxint] * len(v)
	while i < a:
		#find min to make i cents
		coins1 = changeSlow(v, c, i, level+1)

		#find min to make a - i cents
		coins2 = changeSlow(v, c, a - i, level+1)
		
		if sum(coins1) <= sum(minCoins):
				minCoins = coins1
		if sum(coins2) <= sum(minCoins):
				minCoins = coins2
		i = i + 1
	
	print "Min Coins: ", minCoins
	return minCoins




money = open("Coin1.txt", 'r')
#sys.stdout = open("changeResults.txt", "w")

amount = [0]

while True:
	values = money.readline()
	if not values:
		break
	if values == [''] or values[0] == '#' or values[0] == '\n':
		continue
	amount = int(money.readline())
	print "Amount: ", amount
	
	values = values.rstrip('\n')
	values = values.rstrip('\r')
	values = values.rstrip(']')
	values = values.lstrip('[')
	values = values.split(',') 
	values = map(int, values)
	print "Denominations: ", values
	coinCount = [0] * len(values)
	coinCount = changeSlow(values, coinCount, amount, 0)
	print "Coins: ", coinCount
	print

money.close()
