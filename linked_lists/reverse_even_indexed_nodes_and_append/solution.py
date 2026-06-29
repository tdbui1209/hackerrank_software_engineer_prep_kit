def extractAndAppendSponsoredNodes(head):
    odd_head = odd_tail = None
    even_head = None
    
    idx = 0
    cur = head
    while cur:
        nxt = cur.next
        cur.next = None
        if idx % 2 == 0:
            cur.next = even_head
            even_head = cur
        else:
            if odd_head is None:
                odd_head = odd_tail = cur
            else:
                odd_tail.next = cur
                odd_tail = cur
        idx += 1
        cur = nxt
    
    if odd_head is None:
        return head
    odd_tail.next = even_head
    return odd_head
