import sys
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # power = math.floor(math.log(sys.maxsize, 3))
        return n > 0 and 4052555153018976267 % n == 0
