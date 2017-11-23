class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        
        # Missing integers are between 1 to len(n)
        index = 0
        # Swap with index
        while index < len(nums):
            # If current number is between 1 to n, then its indexable, swap current number with nums @ current number
            # Python's lazy so the second condition is guaranteed not to fail
            current_num = nums[index]
            if (1 <= current_num <= len(nums)) and nums[current_num - 1] != current_num:
                nums[index], nums[current_num - 1] = nums[current_num - 1], nums[index]
            else: index += 1
        
        missing = 1
        for num in nums:
            if num != missing: return missing
            # Increment counter
            missing += 1
        return missing
    
        # [2,1,4] => [1,2,4] return 3
        # [1,8,3,1,1,1] return 2
