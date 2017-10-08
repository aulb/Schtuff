#https://discuss.leetcode.com/topic/17510/4-7-lines-python
#https://discuss.leetcode.com/topic/16388/simple-python-dfs-solution-with-explanation
#http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-whilst-preserving-order
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def generateParenthesis(n):
	"""
	:type n: int
	:rtype: List[str]
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
	return lookup[n]
