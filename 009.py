class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        negatives are false
        divisible by 10 are also not palindromic
        
        while one number is bigger
        while not half, convert only half
        x = 1337
        x % 10 = 7
        x / 10 = 133
        return x
        """
        if x < 0 or (x % 10 is 0 and x is not 0):
            return False
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x / 10
        return x == (result / 10) or x == result