from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # # I like the sorting approach, extra O(n) space
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        # return s == t
        
        # # Hash table
        c = Counter()
        for char in s:
            counter = c.get(char, 0)
            c[char] = counter + 1
        
        for char in t:
            counter = c.get(char, 0)
            c[char] = counter - 1
            if c[char] < 0: return False
        
        # Need to count        
        return sum(c.values()) == 0
