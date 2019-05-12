class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0)
    dummyHead.next = head
    l1 = head
    l2 = l1.next
    head = l2
    while l2:
        dummyHead.next = l2
        l1.next = l2.next
        l2.next = l1

        if l1.next and l1.next.next:
            dummyHead=l1
            l1 = l1.next
            l2 = l1.next
        else:
            break
    return head