class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # incorrect algorithm
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #
    #     dummyHead = ListNode(0)
    #     dummyHead.next = l1
    #     count = 0
    #     while (l1 != None and l2 != None):
    #
    #         sum = l1.val + l2.val
    #         if sum >= 10:
    #             l1.val = sum % 10 + count
    #             count = 1
    #         else:
    #             l1.val = sum + count
    #             count = 0
    #         if l1.next == None and l2.next != None:
    #             l2=l2.next
    #             l2.val+=count
    #             if count==1 and l2.next!=None:
    #                 l2.next.val+=1
    #             l1.next = l2
    #             return dummyHead.next
    #         elif l1.next != None and l2.next == None:
    #             l1=l1.next
    #             l1.val += count
    #             return dummyHead.next
    #         elif l1.next == None and l2.next == None:
    #             if count==1:
    #                 head=ListNode(1)
    #                 l1.next=head
    #                 return dummyHead.next
    #         l2 = l2.next
    #         l1 = l1.next
    #     return dummyHead.next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        l3 = dummyHead
        count = 0
        while (l1 or l2):
            if l1 == None:
                sum = l2.val + count
                l3.next = ListNode(sum % 10)
                count = 1 if sum >= 10 else 0
                l3 = l3.next
                l2 = l2.next
            elif l2 == None:
                sum = l1.val + count
                l3.next = ListNode(sum % 10)
                count = 1 if sum >= 10 else 0
                l3 = l3.next
                l1 = l1.next
            else:
                sum = l1.val + l2.val + count
                l3.next = ListNode(sum % 10)
                count = 1 if sum >= 10 else 0
                l3 = l3.next
                l1 = l1.next
                l2 = l2.next
        if count==1:
            l3.next=ListNode(count)
        return dummyHead.next


p = Solution()
l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(4)
l = ListNode(0)
l.next = p.addTwoNumbers(l1, l2)
while (l.next != None):
    l = l.next
    print(l.val)
