def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    cur=head

    while cur.next:
        pre = cur.next
        if cur.val==pre.val:
            pre=pre.next
            cur.next=pre
        if cur.next and pre.val!=cur.val:
            cur=cur.next
    return head