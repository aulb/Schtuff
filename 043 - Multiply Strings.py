class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Positives only
        result = [0] * (len(num1) + len(num2))
        r, n, m = len(result) - 1, len(num1) - 1, len(num2) - 1
        
        for i in range(n, -1, -1): # No reversing needed, save space
            # Temporary variable
            t = r
            for j in range(m, -1, -1):
                result[t] += int(num1[i]) * int(num2[j]) # [0,64]
                result[t - 1] += result[t] // 10         # [0,64] => [6,64]
                result[t] %= 10                          # [6,4]
                t -= 1
            r -= 1
            
        # Get rid of leading zeroes, can't do 'remove zeroes in place' because it will remove all zeroes
        i, start = 0, 0
        # Always remember to check before accessing something
        while i < len(result) and result[i] == 0:
            start += 1
            i += 1
            
        if start == len(result): return '0'
        return ''.join(map(str, result[start:]))
