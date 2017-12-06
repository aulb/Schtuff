class Solution(object):
    def binarySearch(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            med = (lo + hi) // 2
            if nums[med] == target: return med
            if nums[med] > target: hi = med - 1
            else: lo = med + 1
        return -1
                
    def findEdge(self, nums, target, right=False):
        previous = current = self.binarySearch(nums, target)
        while True:
            ending = self.binarySearch(nums[current + 1:] if right else nums[:current], target)
            if ending == -1: return current
            current = current + 1 + ending if right else ending
        
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findEdge(nums, target), self.findEdge(nums, target, True)]
