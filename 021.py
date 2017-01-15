# https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place
# Merge while keeping values sorted
def mergeTwoLists1(self, l1, l2):
    # Build dummy and another pointer
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    # Its already sorted so whichever comes after is sorted
    cur.next = l1 or l2
    # Return starting from the beginning
    return dummy.next