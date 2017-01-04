#!/usr/bin/env python
"""
Given a list of sorted integers, find two integers that sums to k.
"""

def two_int_sum(A, k):
	# O(nlogn)
	midpoint = k / 2

	# Binary search strategy
	first = 0
	last = len(A) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if A[midpoint] == item:
			found = True
		else:
			if item < A[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	

	return -1


if __name__ == '__main__':
	pass