# ALPHANUMERIC
import re

alphanumeric = re.compile(r'[a-z0-9]')

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not s: return True # covered 
        s = s.lower()
        lo, hi = 0, len(s) - 1
        
        print(s)
        while lo <= hi:
            if not alphanumeric.match(s[lo]):
                lo += 1
            elif not alphanumeric.match(s[hi]):
                hi -= 1
            else:                
                if s[lo] != s[hi]: return False

                # Don't forget to advance the pointers
                lo += 1
                hi -= 1
        return True
