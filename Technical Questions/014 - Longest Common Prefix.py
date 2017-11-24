class Solution(object):
    def longestCommonPrefix(self, strings):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strings) is 0:
            return ''
            
        common = [s for s in strings[0]]
        for string in strings:
            t = []
            string = [s for s in string]
                    
            for i in zip(common, string):
                if i[0] == i[1]:
                    t.append(i[0])
                else:
                    break
                
            common = t
        return ''.join(common)
