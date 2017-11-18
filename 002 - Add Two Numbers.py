# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(0)
        carry = 0
        
        while l1 or l2:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            remainder = value % 10
            # Need to keep track of carry if its more than 9
            carry = 1 if value > 9 else 0
            
            new_node = ListNode(remainder)
            dummy.next = new_node
            dummy = new_node
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry: dummy.next = ListNode(carry)
        
        return head.next



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def toInt(l):
    n = []

    n.append(str(l.val))
    while l.next is not None:
        l = l.next
        n.append(str(l.val))

    print n
    return int(''.join(n[::-1]))

# OLD NOPE
# def addTwoNumbers(l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     string = str(toInt(l1) + toInt(l2))
#     string = string[::-1]
#     head = ListNode(string[0])
#     strlen = len(string)
#     for i in range(1, strlen):
#     	next = ListNode(string[i])
#     	head.next = next
#     	head = head.next

#     return head


# if __name__ == '__main__':
# 	l1 = ListNode(1)
# 	l1.next = ListNode(2)
# 	l1.next.next = ListNode(3)
# 	l2 = ListNode(3)
# 	l2.next = ListNode(2)
# 	l2.next.next = ListNode(1)
# 	print addTwoNumbers(l1, l2)
