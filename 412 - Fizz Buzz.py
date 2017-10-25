#!/usr/bin/env python
# PYTHON 2 ALERT
from fractions import gcd

def lcm(a, b):
	return (a * b) // gcd(a, b)

# <strike>Fizzbuzz</strike> Cracklepop with more crackle popping.
def fizzbuzz(numlist, crackle, pop):
	cracklepop = lcm(crackle, pop)
	for n in numlist:
		if not n % cracklepop:
			print 'CracklePop'
		elif not n % crackle:
			print 'Crackle'
		elif not n % pop:
			print 'Pop'
		else:
			print n

if __name__ == '__main__':
	crackle = 3
	pop = 5
	numlist = range(1, 101)

	# I just realized after writing this that 
	# there is more than lcm and divisibility
	# properties than cracklepops
	fizzbuzz(numlist, crackle, pop)


"""
class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                result.append('FizzBuzz')
            elif not i % 3:
                result.append('Fizz')
            elif not i % 5:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
"""
