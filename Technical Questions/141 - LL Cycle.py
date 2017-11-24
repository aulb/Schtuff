# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        # Rabbit + hare, run at different speed, one will eventually catch up
        # Fast, slow pointer, until they meet
        # Reset fast pointer to the beginning
        # Advance until meet again
        # None?
        slow, fast, = head
        while fast and slow and fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

"""
slow, fast = head, head.next
while slow != fast:
    if not (fast and fast.next): return False
    slow = slow.next
    fast = fast.next.next
return True
"""
