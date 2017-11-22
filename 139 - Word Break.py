class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s: return False
        # "hello"
        # he, hel, llo
        
        # length string: i
        # length array: n elements
        # length of longest string in the array: j
        # O(i*n*j)
        lookup = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i - len(word) + 1: i + 1] == word and ((i - len(word) == -1) or lookup[i - len(word)]):
                    lookup[i] = True
            print(lookup)

        return lookup[-1]
