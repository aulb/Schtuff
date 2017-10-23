# difference in len
# advance the one with longest to equal len

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def getLength(self, head):
		counter = 0
		while head:
			counter += 1
			head = head.next
		return counter


	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		aLength = self.getLength(headA)
		bLength = self.getLength(headB)

		diff = abs(aLength - bLength)

		while diff > 0:
			diff -= 1
			if aLength > bLength: headA = headA.next
			else: headB = headB.next

		toggle = True
		while headA and headB:
			if headA == headB: return headA
			if toggle: headA = headA.next
			else: headB = headB.next
			toggle = not toggle

		return None
