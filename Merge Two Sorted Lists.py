# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0)
    head = dummyHead
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = ListNode(l1.val)
            l1=l1.next
        else:
            head.next = ListNode(l2.val)
            l2=l2.next
        head = head.next
    if l1 == None:
        head.next = l2
    elif l2 == None:
        head.next = l1
    return dummyHead.next


l1 = ListNode(4)
l1.next = ListNode(5)
l1.next.next = ListNode(6)
l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

l3 = ListNode(0)
l3.next = mergeTwoLists(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next
