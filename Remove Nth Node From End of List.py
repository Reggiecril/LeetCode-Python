
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummyHead=ListNode(0)
    dummyHead.next=head
    first_ptr=dummyHead
    second_ptr=head

    for i in range(1,n):
        second_ptr=second_ptr.next
    while second_ptr.next:
        second_ptr=second_ptr.next
        first_ptr=first_ptr.next
    l1=first_ptr.next
    l1=l1.next
    first_ptr.next=l1
    return dummyHead.next




class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1=ListNode(1)
# l1.next=ListNode(2)
# l1.next.next=ListNode(3)
# l1.next.next.next=ListNode(4)
# l1.next.next.next.next=ListNode(5)
result=ListNode(0)
result.next=removeNthFromEnd(l1,1)
while result.next:
    result=result.next
    print(result.val)