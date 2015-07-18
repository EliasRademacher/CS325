def greedy(a, v):
	change = [0] * len(v)
	temp = 0
	for e in reversed(v):
		while((temp + e) <= a):
			temp += e
			change[v.index(e)] = change[v.index(e)] + 1
	return change