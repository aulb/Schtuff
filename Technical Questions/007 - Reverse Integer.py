class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return x
        # Negative flag
        is_negative = x < 0    
        x = abs(x) # Modified x
        result = 0
        while x != 0:
            result *= 10 # Multiple first to accomodate
            result += x % 10 	
            x = x // 10			
        if result > 2**31 - 1: return 0 # LEETCODE ONLY REQUIREMENT
        return -result if is_negative else result
