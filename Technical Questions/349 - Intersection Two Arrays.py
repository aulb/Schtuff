# set(nums1), set(num2) list(nums1 & nums2)
# Better method?? O(m + n) space
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not (nums1 and nums2): return []
        
        # nums1 and nums2 not guaranteed sorted arrays
        result = set()
        lookup = set(nums1)
        
        for num in nums2:
            if num in lookup: result.add(num)
                
        return list(result)
