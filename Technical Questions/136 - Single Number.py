from functools import reduce
# Naive: Use a hash, once the count for an element 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
# There is an operator.xor for lambda
# https://docs.python.org/2/library/operator.html
""" FROM THE SOLUTIONS:
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)

>>> set([1,2,3]) 
{1,2,3}
>>> set([1,2,3,3])
{1,2,3}
>>> set([1,1,1,1,1,2,3,3,3,3,3,3,3])
{1,2,3}
"""
