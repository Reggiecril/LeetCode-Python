def rotateRight(head, k):
    l3 = head
    length = 1
    while l3.next:
        length += 1
        l3 = l3.next
    k %= length
    if k == 0:
        return head
    l3.next=head
    l2=head
    for i in range(k):
        l2=l2.next
        l3=l3.next
    l3.next=None
    return l2