"""
class LinkedList:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next
	def __repr__(self):
		return 'LinkedList({}, {})'.format(self.value, repr(self.next))


def reverse(item, tail = None):
	next = item.next
	item.next = tail
	if next is None:
		return item
	else:
		return reverse(next, item)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        while head:
            head_next = head.next
            head.next = previous
            previous, head = head, head_next
            
            # previous, head, head.next = head, head.next, previous # EXPLORE
        	
        return previous
