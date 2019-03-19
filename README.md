# LeetCode-Practice

##### This is just a practice for LeetCode by Python. Author By [Reggiecril](https://github.com/Reggiecril).
***
+ Two Sum
```python
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        length=len(nums)
        count=0
        while(count<length):
            if target-nums[count] in dict:
                return [dict[target-nums[count]],count]
            dict[nums[count]]=count
            count+=1
```
***
+ Add Two Numbers
```python
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

```
