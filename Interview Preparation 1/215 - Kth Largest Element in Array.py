from random import randint
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Assumptions
        ## k is between 1 < len(nums)
        ## nums is not empty
        return self.findKthLargestAux(nums, 0, len(nums) - 1, k)
    
    def findKthLargestAux(self, nums, left, right, k):
        pivot = nums[randint(left, right)]
        starting_left, starting_right = left, right
        
        while left <= right:
            # if nums[left] <= pivot then its on the correct spot
            if nums[left] > pivot: # nums[left] should be on the right side
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            # if nums[right] > pivot then its on the correct spot
            elif nums[right] <= pivot: # nums[right] should be on the left side
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                left += 1
                right -= 1
        
        # left is how many elements are lesser than or equal to "pivot" 
        if left == k: return min(nums[starting_left:left])
        elif left > k: return self.findKthLargestAux(nums, starting_left, left, k)
        else: return self.findKthLargestAux(nums, left, starting_right, k - left)
