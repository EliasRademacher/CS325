
def greedy(v, a):
	change = [0] * len(v)
	temp = 0
	for e in reversed(v):
		while((temp + e) <= a):
			temp += e
			change[v.index(e)] = change[v.index(e)] + 1
	return change
	
change = greedy([1, 3, 7, 12], 29)
print "change: ", change