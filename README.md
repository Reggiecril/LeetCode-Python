# LeetCode-Practice

##### This is just a practice for LeetCode by Python. Author By [Reggiecril](https://github.com/Reggiecril).
***
##### 1. Two Sum
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
##### 2. Add Two Numbers
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
***
##### 3. Longest Substring Without Repeating Characters
```python
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        collect = []
        length = 0
        for i in s:
            if i in collect:
                collect = collect[collect.index(i)+1:]
                collect.append(i)
            else:
                collect.append(i)
            length=max(len(collect),length)

```
***
##### 9. Palindrome Number
```python
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10 and x > 0:
            return True
        x = str(x)
        length = len(x)
        count = 0
        while count < length / 2 + 1:
            first = x[count]
            last = x[length - 1 - count]
            if not first.__eq__(last):
                return False
            count += 1
        return True
    ###Best Solution
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False

```
***
##### 11. Container With Most Water
```python
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        startPtr=0
        lastPtr=len(height)-1
        sum=0
        while lastPtr>startPtr:
            sum=max(sum,min(height[lastPtr],height[startPtr])*(lastPtr-startPtr))
            if height[lastPtr]>height[startPtr]:
                startPtr+=1
            elif height[startPtr]>height[lastPtr]:
                lastPtr-=1
            else:
                startPtr+=1
                lastPtr-=1
        return sum

```
***
##### 35. Search Insert Position

```python
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1
        if target > nums[len(nums) - 1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

```
***
##### 19. Remove Nth Node From End of List

```python

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

```
***
##### 22. Generate Parentheses


```python

    class Solution(object):
        def generateParenthesis(self,n):
            """
            :type n: int
            :rtype: List[str]
            """
            p_list=[]
            self.getParenthesis('', p_list, 0, 0, n);
            return p_list
    
    
        def getParenthesis(self,string, p_list, o, c, n):
            if c == n:
                p_list.append(string)
            else:
                if o > c:
                    self.getParenthesis(string + ')', p_list, o, c + 1, n)
    
                if o < n:
                    self.getParenthesis(string + '(', p_list, o + 1, c, n)


```
***
##### 21. Merge Two Sorted Lists


```python
    class Solution(object):
        def mergeTwoLists(self, l1, l2):
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
```
***
##### 27. Remove Element


```python
    class Solution(object):
        def removeElement(self, nums, val):
            """
            :type nums: List[int]
            :type val: int
            :rtype: int
            """
            number = nums.count(val)
            if number != 0:
                while number > 0:
                    nums.remove(val)
                    number -= 1
            return len(nums)
```
***
##### 24. Swap Nodes in Pairs


```python
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
```
***
##### 70. Climbing Stairs


```python
   def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        list=[]
        for i in range(n):
            if i==0:
                list.append(1)
            elif i==1:
                list.append(2)
            else:
                list.append(list[i-1]+list[i-2])
        return list[n-1]
```
***
##### 100. Same Tree

```python
   def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None or q == None:
            return q == p
        # return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        else:
            return False

```
***
##### 104. Maximum Depth of Binary Tree

```python
   def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        # if root.left == None and root.right == None:
        #     return 1
        # elif root.left == None and root.right != None:
        #     return self.maxDepth(root.right) + 1
        # elif root.right == None and root.left != None:
        #     return self.maxDepth(root.left) + 1
        # else:
        #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        

```
***
##### 59. Spiral Matrix II

```python
       def generateMatrix(n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        list = [[0 for i in range(n)] for i in range(n)]
        left = 0
        right = n
        top = 0
        bottom = n
        count = 0
        while count<n*n:
            for i in range(right-left):
                list[top][left+i] = count + 1
                count += 1
            top += 1
            for i in range(bottom-top):
                list[top+i][right-1] = count + 1
                count += 1
            right -= 1
            for i in range(right-left):
                list[bottom-1][right-i-1]=count+1
                count+=1
            bottom-=1
            for i in range(bottom-top):
                list[bottom-1-i][left]=count+1
                count+=1
            left+=1
        #
        # n -= 1
        for i in range(n):
            print(list[i], '\n')

```