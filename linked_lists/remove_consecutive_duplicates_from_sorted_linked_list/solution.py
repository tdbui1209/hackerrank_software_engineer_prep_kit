def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.next.data == cur.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
