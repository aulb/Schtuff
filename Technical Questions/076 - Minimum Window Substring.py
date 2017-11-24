from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not (t and s): return ''
        
        shortest_string = None
        
        count = len(t)
        counter = Counter(t)
        
        start, end = 0, 0
        while end < len(s):
            if s[end] in counter:
                counter[s[end]] -= 1
                count -= 1
            if count == 0:
                if len(shortest_string) > len(s[start:end + 1]):
                    shortest_string = s[start:end + 1]
                    
                if s[start] not in counter: start += 1
                else: pass
                    
                    
            
        return shortest_string
