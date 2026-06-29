def removeKthNodeFromEnd(head, k):
    slow = fast = head
    for _ in range(k + 1):
        if fast is None:
            return head
        fast = fast.next
    
    if fast is None:
        return head.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
