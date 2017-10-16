# set(nums1), set(num2) list(nums1 & nums2)
# Better method?? O(m + n) space
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        result = []
        for i in nums1:
            d1[i] = True
        for i in nums2:
            # Same values...
            if d1.get(i, False) and not d2.get(i, False):
                result.append(i)
            d2[i] = True
        return result
