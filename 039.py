def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
	if n == 0:
		return ''

	# Build lookup	
	lookup = {0: [''], 1: ['()']}
	for _ in range(2, n + 1):
		curr = []    		
		# Do case q = 0
		for s in lookup[_ - 1]:
			curr.append('(' + s + ')')

		for i in range(1, _):
			q = _ - i
			print _, q
			for s1 in lookup[q]:
				for s2 in lookup[_ - q]:
					curr.append(s1 + s2)
		# Append after pruning 
		lookup[_] = f7(curr)
	return lookup