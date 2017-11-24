from functools import reduce
# 8 = 1000
# 7 = 0111
# n & n - 1 => 0 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)
        # if n < 1: return False
        # return reduce(lambda x, y: int(x) + int(y), "{0:b}".format(n) + '0') == 1
