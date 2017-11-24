class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # so_far = [None] * len(nums) # At most
        if not nums: return []
        result = [[]]

        def fill_result(index, current_result=[]):
            if index >= len(nums): return
            current_result = current_result[::]
            
            # Don't add anything
            fill_result(index + 1, current_result)
            current_result.append(nums[index])
            # Add the current index
            fill_result(index + 1, current_result)
            result.append(current_result)
            
        fill_result(0)
        return result
