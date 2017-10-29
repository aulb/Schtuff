from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = Counter()
        for num in nums:
            count = counter.get(num, 0)
            if count > 0: return True
            counter[num] = count + 1
        return False
