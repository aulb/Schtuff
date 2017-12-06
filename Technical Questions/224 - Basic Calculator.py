class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        return self._calculate(s, 0)[0]
    
    def perform_operation(self, operator, accumulator, digit):
        if operator == '+' or operator == '':
            accumulator += int(digit)
        else:
            accumulator -= int(digit)
        return accumulator
    
    def _calculate(self, s, start):
        operator = ''
        result = 0
        digit = ''
        
        index = start
        while index < len(s):
            token = s[index]
            if token.isdigit(): digit += token
            elif token == '+' or token == '-': 
                # if operator is empty, add digit to accumulator
                if digit: result = self.perform_operation(operator, result, digit)
                # update the operator
                operator = token
                # reset the digit
                digit = ''
            elif token == '(':
                intermediate_value, index = self._calculate(s, index + 1)
                result = self.perform_operation(operator, result, intermediate_value)
                continue
            elif token == ')':
                # check if digit is populated, check operator, we need to return immediately
                if digit: result = self.perform_operation(operator, result, digit)
                return result, index + 1
                
            # Always increment
            index += 1
            
        # check at the very end
        if digit: result = self.perform_operation(operator, result, digit)
            
        return result, index
