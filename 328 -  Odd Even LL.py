# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.EVEN = 0
        self.ODD = 1
    
    def findNext(self, node, counter, remainder):
        # Assuming this one isn't already 
        if not node: return node, counter
        
        while node and node.val % 2 != remainder:
            node = node.next
            counter += 1
        
        return node, counter
    
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Assume all nodes has integer as its value, find starting odd and even
        odd, oc = self.findNext(head, 0, self.ODD)
        even, ec = self.findNext(head, 0, self.EVEN)
        
        while odd and even:
            print(oc, odd.val, ec, even.val)
            if oc > ec:
                # If odd is ahead in counter, swap even with odd
                # even is now odd, and odd is now even
                odd.val, even.val = even.val, odd.val
                # find the next odd and the next even
                odd, oc = self.findNext(odd.next, oc + 1, self.ODD)
                even, ec = self.findNext(even.next, ec + 1, self.EVEN)
            else:
                # If even is ahead, find the next odd, they can't be the same
                odd, oc = self.findNext(odd.next, oc + 1, self.ODD)
            
            
        return head
