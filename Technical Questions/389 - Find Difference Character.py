class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = {}
        for ch in s:
            # No need for initialization
            cnt[ch] = cnt.get(ch, 0) + 1
            
        for ch in t:
            if cnt.get(ch, 0) == 0:
                return ch
            else:
                cnt[ch] -= 1
