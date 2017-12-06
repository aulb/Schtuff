from collections import deque
class Solution:
    def array_shift(self, array):
        start = 0
        for index, value in enumerate(array):
            if value is not None: 
                array[index], array[start] = array[start], array[index]
                start += 1
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Easier without spaces
        s = s.replace(' ', '')
        numbers, operators = [], []
        
        digits = ''
        # Parse the expression into the two stacks, len(numbers) = len(operators) + 1 guaranteed
        for token in s:
            if token.isdigit(): digits += token
            else:
                if digits:
                    numbers.append(int(digits))
                    digits = ''
                operators.append(token)
        if digits: numbers.append(int(digits))     
            
        # Do the more sensitive * and /
        for index, operator in enumerate(operators):
            if operator == '/' or operator == '*':
                numbers[index + 1] = numbers[index] // numbers[index + 1] if operator == '/' else numbers[index] * numbers[index + 1]            
                numbers[index] = None
                operators[index] = None

        # Shift the zeroes to the end
        self.array_shift(numbers) 
        self.array_shift(operators)
        
        for index, operator in enumerate(operators):
            if not operator: return numbers[0]
            if operator == '+':
                numbers[0] += numbers[index + 1]
            else:
                numbers[0] -= numbers[index + 1]
        
        return numbers[0]
