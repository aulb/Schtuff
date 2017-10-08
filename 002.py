"""
https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# 7:30 - 8:00

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


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    string = str(toInt(l1) + toInt(l2))
    string = string[::-1]
    head = ListNode(string[0])
    strlen = len(string)
    for i in range(1, strlen):
    	next = ListNode(string[i])
    	head.next = next
    	head = head.next

    return head


if __name__ == '__main__':
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(3)

	l2 = ListNode(3)
	l2.next = ListNode(2)
	l2.next.next = ListNode(1)


	print addTwoNumbers(l1, l2)
