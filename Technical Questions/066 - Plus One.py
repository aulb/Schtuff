class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        [1,2,3] => [1,2,4]
        [0] => [1]
        [9,9,9] => [1,0,0,0]
        """
        # Iterate backwards
        carry = 1 
        for i in range(len(digits) - 1, -1, -1):
            # Add the carry to the digit
            plus_one = digits[i] + carry
            # If the remainder is above 0 that means theres a carry
            digits[i] = (plus_one) % 10
            # Update the carry
            carry = 1 if plus_one > 9 else 0        
            
        # Append 1 to the beginning of the array
        if carry == 1:
            return [1] + digits
        return digits
