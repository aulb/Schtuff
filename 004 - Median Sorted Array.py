"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
8:52 9:00*  | 9:34
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Brute force
        # If even, return / 2
        # The median is on (n + m - 1) / 2
        # nums1[m / 2]


        # The median for nums2 = 1 @2 
        # The median for nums3 = 3 @1

        # 3 > 1 so search in nums1
        # 2 / 2 = 1 => 2
        # 1 / 2 = 0 => 1 its equal, then that means return 2
        # Otherwise return (1 + 2) / 2


        # [1] + [1,1,1,1,1,1,1,2,3,4,5]

        m = len(nums1)
        n = len(nums2)
        mid1 = m / 2
        mid2 = n / 2
        while True:	
	        if nums1[mid1] < nums2[mid2]:
	        	# Update midpoint for the second one
	        	mid2 = mid2 / 2
	       	elif nums1[mid1] > nums2[mid2]
	       		mid1 = mid1 / 2
	       	else:
	       		# They're equal
	       		break

        



          #       7 = 3
  #       m / 2
  #       [1,2,3,4,5]
  #       5 / 2 = 2
		# 3

  #       n / 2
  #       [1,1]
  #       2 / 2 = 1
  #       1
