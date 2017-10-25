# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """ # Base case covered
        # Find midpoint
        fast = slow = head
        # Slow will be the midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Reverse anything from slow, we can discard fast
        previous = None
        while slow:
            # Switch these two
            previous, slow.next = slow.next, previous
            previous, slow = slow, previous
        
        while head and previous:
            if head.val != previous.val: return False
            head = head.next
            previous = previous.next
            
        return True
