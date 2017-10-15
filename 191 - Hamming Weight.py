def hammingWeight(n):
	return len(filter(lambda chr: int(chr), '{0:b}'.format(n)))
