class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        s = s.upper() # Make sure all uppercase
        
        result = 0
        for index in range(len(s) - 1, -1, -1): 
            result += (ord(s[index]) - 64) * 26 ** (len(s) - 1 - index)
            
        return result
