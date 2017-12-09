from collections import deque
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        result = deque([''])
        digit_map = {
            '0': ' ',
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'             
        }
        
        # length ==> length so far
        for length, digit in enumerate(digits):
            while result and len(result[0]) == length:
                temp_string = result.popleft()
                for char in digit_map[digit]:
                    result.append(temp_string + char)
        return list(result)
