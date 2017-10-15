def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # current = head
    # while current:
    #     while current.next and current.val == current.next.val:
    #         current.next = current.next.next
    #     current = current.next
    # return head

    current = None
    next = head
    while next:
        current = next # head
        next = next.next # head.next
        while next and next.val == current.val: # head.next.val == head.val # need to check if next is also null
            next = next.next # head.next = head.next.next <--
            # if it becomes null, next.val doesn't exist...
        current.next = next # head.next = head.next...
        
    return head

