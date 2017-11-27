# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

## ORDER OF CHECKING MATTERS 
## COMPARATORS MATTERS
from random import randint
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Assumptions:
        ## k is between 1 and len(nums)
        ## nums is not empty
        ## nums contain only unique elements
        if not nums: return 
        return self.findKthSmallest(nums, len(nums) + 1 - k)
            
    # Attempts to sort in descending order
    def findKthSmallest(self, nums, k):
        left, right = 0, len(nums) - 1
        pivot = nums[randint(left, right)]

        while left <= right:
            # if nums[right] > pivot then its on the correct spot
            if nums[right] <= pivot: # nums[right] should be on the left side
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # if nums[left] <= pivot then its on the correct spot
            elif nums[left] > pivot: # nums[left] should be on the right side
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
                right -= 1
                
        # There will be `left` numbers that are less than or equal to pivot
        if left == k: return max(nums[:left]) 
        elif left > k: return self.findKthSmallest(nums[:left], k)
        else: return self.findKthSmallest(nums[left:], k - left)
