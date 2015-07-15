greedy(v, a):
	change = [] * len(v)
	for e in reversed(v):
		while((sum(change) + e) < v):
			#index is wrong because of reversed list __maybe__
			change[v.index(e)] = change[v.index(e)] + e
	return change