# from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        current_num = nums[0]
        count_yes, count_no = 1, 0
        index = 1
        while index < len(nums):
            if nums[index] != current_num:
                count_no += 1
                if count_yes == count_no:
                    # Reset
                    current_num = nums[index]
                    count_yes, count_no = 1, 0
            else: count_yes += 1
            index += 1

        return current_num if self.is_majority(nums, current_num) else -1

    def is_majority(self, nums, num):
        return nums.count(num) > len(nums) // 2        

        # Always check for error
        # [2,1] return any
        # [2,2,3] return 2 because it appears more than once
        # # Not O(1) space
        # counter = Counter()
        # for num in nums:
        #     counter[num] += 1
        
        # majority = counter.most_common(1)
        # return majority[0][0]
