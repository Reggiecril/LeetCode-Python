# LeetCode-Practice

##### This is just a practice for LeetCode by Python. Author By [Reggiecril](https://github.com/Reggiecril).
###### I used two language under this project. First time i used Pyhton to do it, but i mention Python have too good package that i can not clear to learn data strucutre, so i changed it to Java.
***
##### 1. Two Sum
```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 2. Add Two Numbers
```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 3. Longest Substring Without Repeating Characters
```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 5. Longest Palindromic Substring

```python
	# Edit By <font color=#0099ff>Python</font>
    # only 22%
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s),0,-1):
            for j in range(len(s)-i):
                res=s[j:i+j]
                if res==res[::-1]:
                    return res
        return ""

```
***
***
##### 6. ZigZag Conversion


```python
	# Edit By <font color=#0099ff>Python</font>

    #98%
    def convert(self, s: str, numRows: int) -> str:
        if s == "" or numRows == 1:
            return s
        l = ['']*numRows
        index, step = 0, 1
        for i in s:
            l[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(l)
    
```
***
***
##### 7. Reverse Integer


```java
    #Edit By Java
    #100%
     public int reverse(int x) {
            int sign = (x > 0) ? 1 : -1;
            long g = Math.abs(x);
            long re = 0;
            while (g > 0) {
                long count = g % 10;
                re = re * 10 + count;
                g /= 10;
            }
            if (re * sign > Integer.MAX_VALUE)
                return 0;
            else if (re * sign < Integer.MIN_VALUE)
                return 0;
            return (int) re * sign;
        }
    
```
***
***
##### 8. String to Integer (atoi)

```python
	# Edit By <font color=#0099ff>Python</font>

    #99%
    def myAtoi(str: str) -> int:
        if not str or len(str.lstrip())==0 or len(str)==0:
            return 0
        str = str.lstrip()
        minus = 1
        if str[0] == "-":
            str = str.replace("-", "", 1)
            minus = -1
        elif str[0] == "+":
            str = str.replace("+", "", 1)
    
            minus = 1
        dig=0
        for i in str:
            if not i.isdigit():
                return dig*minus
            dig=dig*10+int(i)
            if minus==1 and dig>2147483647:
                return 2147483647
            elif minus==-1 and dig>2147483648:
                return -2147483648
        return dig*minus
    
```
***
***
##### 9. Palindrome Number
```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 11. Container With Most Water
```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 13. Roman to Integer
```java
	# Edit By JAVA
     public int romanToInt(String s) {
            if(s=="" || s.length()==0)return 0;
            Map<Character, Integer> map = new HashMap<Character, Integer>();
            map.put('I', 1);
            map.put('V', 5);
            map.put('X', 10);
            map.put('L', 50);
            map.put('C', 100);
            map.put('D', 500);
            map.put('M', 1000);
            int sum=0;
            int pre=0;
            for(int i=s.length()-1;i>=0;i--){
                int cur=map.get(s.charAt(i));
                sum+=(pre>cur)?-cur:cur;
                pre=cur;
            }
            return sum;
        }

```
***
***
##### 12. Integer to Roman
```java
	public String intToRoman(int num) {
            // 100%
            int[] values={1000,900,500,400,100,90,50,40,10,9,5,4,1};
            String[] strs={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
            StringBuilder sb = new StringBuilder();
            for(int i=0;i<values.length;i++){
                while(num>=values[i]){
                    num-=values[i];
                    sb.append(strs[i]);
                }
            }
            return sb.toString();
            
            // #82%
            // //0000,1000,2000,3000
            // String M[] = {"", "M", "MM", "MMM"};
            // //000,100,200,300,400,500,600,700,800,900
            // String C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
            // //00,10,20,30,40,50,60,70,80,90
            // String X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
            // //0,1,2,3,4,5,6,7,8,9
            // String I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
            // return M[num/1000]+C[(num%1000)/100]+X[(num%100)/10]+I[num%10];
        }

```
***
***
##### 14. Longest Common Prefix


```python
	# Edit By <font color=#0099ff>Python</font>
    #100%
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==None or len(strs)==0:
            return ""
        maxs = max(strs)
        mins = min(strs)
        s=""
        for i in range(len(mins)):
            if mins[i]==maxs[i]:
                s+=mins[i]
            else:
                return s
        return s
                    

```
***
***
##### 15. 3Sum


```java
    # Edit By JAVA
	 public List<List<Integer>> threeSum(int[] nums) {
            if(nums.length<3 || nums==null)
                return new ArrayList<>();
            Set<List<Integer>> outList=new HashSet<>();
            Arrays.sort(nums);
            for (int i = 0; i < nums.length; i++) {
                if (i>0 && nums[i]==nums[i-1])
                    continue;
                int pre=nums[i];
                Map<Integer,Integer> map=new HashMap<>();
                for (int j = i+1; j < nums.length; j++) {
                    int value=nums[j];
                    int diff=-(pre+value);
                    if (map.containsKey(diff)){
                        outList.add(Arrays.asList(pre,nums[map.get(diff)],value));
    
                    }else{
                        map.put(value,j);
                    }
    
                }
            }
            return new ArrayList<>(outList);
        }
                    

```
***
***
##### 17. Letter Combinations of a Phone Number

```python
	# Edit By <font color=#0099ff>Python</font>

    #99%
    def letterCombinations(digits: str):
        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'qprs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        list=[""]
        for i in range(len(digits)):
            while len(list[0])==i:
                string=list.pop(0)
                for j in mapper[digits[i]]:
                    list.append(j+string)
        return list
    
```
***
***
##### 19. Remove Nth Node From End of List

```python
	# Edit By <font color=#0099ff>Python</font>

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
***
##### 20. Valid Parentheses

```python
	# Edit By <font color=#0099ff>Python</font>
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        
        # 50%
        # if s=='' or len(s)==0:
        #     return True;
        # l=[]
        # count=0
        # while count<len(s):
        #     if s[count]=='(' or s[count]=='[' or s[count]=='{':
        #         l.append(s[count])
        #     else:
        #         if len(l)==0:
        #             return False
        #         else:
        #             first=l[-1]
        #             second=s[count]
        #             if first=='(' and second==')' or first=='[' and second==']' or first=='{' and second=='}':
        #                 l.pop(-1)
        #             else:
        #                 return False
        #     count+=1
        # return len(l)==0
        # 100%
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "{":
                stack.append("}")
            elif ch == "[":
                stack.append("]")
            else:
                if not stack: return False
                if stack[-1] != ch: return False
                stack.pop()
        return len(stack) == 0

```
***
***
##### 21. Merge Two Sorted Lists


```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 22. Generate Parentheses


```python
	# Edit By <font color=#0099ff>Python</font>

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
***
##### 24. Swap Nodes in Pairs


```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 27. Remove Element


```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 28. Implement strStr()


```python
	# Edit By <font color=#0099ff>Python</font>

    #99%
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:len(needle)+i]==needle:
                return i
        return -1
    
```
***
***
##### 35. Search Insert Position

```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 38. Count And Say

```java
public String countAndSay(int n) {
        if (n==0)
            return "";
        else if (n==1)
            return "1";
        else if(n==2)
            return "11";
        String str="11";
        for (int i = 3; i <= n; i++) {
            int count=0;
            String newStr="";
            for (int j = 0; j < str.length(); j++) {
                if (j==str.length()-1){
                    if (str.charAt(j)==str.charAt(j-1)){
                        count++;
                    }else {
                        newStr+=(String.valueOf(count)+str.charAt(j-1));
                        count=1;
                    }
                    newStr+=(String.valueOf(count)+str.charAt(j));
                    break;
                }
                if (j==0) {
                    count++;
                    continue;
                }
                if (str.charAt(j)==str.charAt(j-1)){
                    count++;
                }else {
                    newStr+=(String.valueOf(count)+str.charAt(j-1));
                    count=1;
                }

            }
            str=newStr;
        }
        return str;
    }
```
***
***
##### 39. Combination Sum

```python
	# Edit By <font color=#0099ff>Python</font>
    
    ################Before Optimize(32%)###############
    def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        in_list = []
        out_list = []
        count = 0
        getSum(candidates, target, in_list, out_list, count)
        return out_list
    
    
    def getSum(candidates, target, in_list, out_list, count):
        while count < len(candidates):
            if target < 0:
                return
            elif target == 0 and in_list not in out_list:
                out_list.append(in_list.copy())
                return
            else:
                in_list.append(candidates[count])
                getSum(candidates, target-candidates[count], in_list, out_list, count)
                in_list.pop()
                count += 1
    ################After Optimize (95%)###############
    def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        in_list = []
        out_list = []
        getSum(sorted(candidates), target, in_list, out_list)
        return out_list
    
    
    def getSum(candidates, target, in_list, out_list):
        if target == 0:
            out_list.append(in_list.copy())
            return
        for i in candidates:
            if target<i:
                break
            if in_list and in_list[-1]>i:continue
            else:
                in_list.append(i)
                getSum(candidates, target-i, in_list, out_list)
                in_list.pop()
    

```
***
***
##### 46. Permutations I

```java
	# Edit By JAVA
    #83%
	public List<List<Integer>> combinationSum2(int[] candidates, int target) {
            List<List<Integer>> list = new ArrayList<>();
            if (candidates == null || candidates.length == 0)
                return list;
            Arrays.sort(candidates);
            combination(candidates, list, new ArrayList<>(), target, 0);
            return list;
        }
    
        private void combination(int[] candidates, List<List<Integer>> outList, List<Integer> inList, int target, int count) {
            if (target == 0) {
                outList.add(new ArrayList<>(inList));
                return;
            }
            if (target < 0) return;
            for (int i = count; i < candidates.length; i++) {
                if (i > count && candidates[i] == candidates[i - 1]) continue;
                inList.add(candidates[i]);
                combination(candidates, outList, inList, target - candidates[i], i + 1);
                inList.remove(inList.size() - 1);
            }
    
    
        }
```
***
***
##### 46. Permutations I

```python
	# Edit By <font color=#0099ff>Python</font>
    #100% but this just for python
	# Edit By <font color=#0099ff>Python</font>3 becuase copy() is not available for python
	# Edit By <font color=#0099ff>Python</font>2
    def permute(nums):
        out_list = []
        permuteCalculation([], out_list, nums, 0, len(nums))
        return out_list

    
    def permuteCalculation(in_list, out_list, nums, count, length):
        if count == length:
            out_list.append(in_list.copy())
            return
        for i in nums:
            in_list.append(i)
            new_num=nums.copy()
            new_num.remove(i)
            permuteCalculation(in_list, out_list, new_num, count+1, length)
            in_list.pop(-1)
        return

                    

```
***
***
##### 47. Permutations II

```python
	# Edit By <font color=#0099ff>Python</font>
    #low efficiency, it is basic algorithm logic
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums==[] or len(nums)==0:
            return []
        list = []
        self.permuteCal(nums, list, [],len(nums))
        return list


    def permuteCal(self,nums, list, num_list,length):
        if len(num_list) == length and num_list not in list:
            list.append(num_list.copy())
            return
        for i in range(len(nums)):
            num_list.append(nums[i])
            new_num = nums.copy()
            new_num.pop(i)
            self.permuteCal(new_num, list, num_list,length)
            num_list.pop(-1)
        return
                    

```
***
***
##### 49. Group Anagrams

```java
	# Edit By JAVA
    #97%
   public List<List<String>> groupAnagrams(String[] strs) {
           List<List<String>> outList=new ArrayList<>();
           if(strs==null||strs.length==0)
               return outList;
           Map<String,List<String>> map=new HashMap<>();
           for(String str:strs){
               char[] ch=str.toCharArray();
               Arrays.sort(ch);
               String newStr=String.valueOf(ch);
               if (map.containsKey(newStr)){
                   map.get(newStr).add(str);
               }else{
                   List<String> inList=new ArrayList<>();
                   inList.add(str);
                   map.put(newStr,inList);
               }
   
           }
           return new ArrayList<>(map.values());
   
       }    

```
***
***
##### 54. Spiral Matrix

```python
	# Edit By <font color=#0099ff>Python</font>
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if matrix==None or len(matrix)==0:
        return matrix
    list=[]
    left=0
    right=len(matrix[0])
    top=0
    bottom=len(matrix)
    count=right*bottom
    while True:
        for i in range(right-left):
            list.append(matrix[top][left+i])
            count-=1
        top += 1
        if count<=0:break
        for i in range(bottom-top):
            list.append(matrix[top+i][right-1])
            count-=1
        right -= 1
        if count <= 0: break
        for i in range(right-left):
            list.append(matrix[bottom-1][right-i-1])
            count-=1
        bottom-=1
        if count <= 0: break
        for i in range(bottom-top):
            list.append(matrix[bottom-1-i][left])
            count-=1
        left+=1
        if count <= 0: break
    return list

```
***
***
##### 55. Jump Game

```python
	# Edit By <font color=#0099ff>Python</font>
    
    def canJump(nums):
        if len(nums)<=1:
            return True
        length = len(nums) - 1
        count = nums[0]
        ptr = 0
        while count >= ptr and ptr <= length:
            count = max(count, nums[ptr] + ptr)
            if count>=length:
                break
            ptr += 1
        return count >= length
```
***
***
##### 58. Length of Last Word


```python
	# Edit By <font color=#0099ff>Python</font>

    def lengthOfLastWord(s: str) -> int:
        if len(s.strip())==0:
            return 0
        return s.strip().split(" ")[-1]

```
***
***
##### 59. Spiral Matrix II

```python
	# Edit By <font color=#0099ff>Python</font>
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
***
***
##### 61. Rotate List


```python
	# Edit By <font color=#0099ff>Python</font>

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
```
***
***
##### 62. Unique Paths

```python
	# Edit By <font color=#0099ff>Python</font>

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        grid = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]

```
***
***
##### 63. Unique Paths II

```python
	# Edit By <font color=#0099ff>Python</font>

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        value = 1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                value = 0
            obstacleGrid[0][i] = value
        value = 1
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                value = 0
            obstacleGrid[i][0] = value
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[j][i] == 1:
                    obstacleGrid[j][i] = 0
                else:
                    obstacleGrid[j][i] = obstacleGrid[j - 1][i] + obstacleGrid[j][i - 1]
    
        return obstacleGrid[-1][-1]

```
***
***
##### 64. Minimum Path Sum



```python
	# Edit By <font color=#0099ff>Python</font>

    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        my_grid=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
       
        my_grid[0][0]=grid[0][0]
        for i in range(1,len(grid)):
            my_grid[i][0]=grid[i][0]+my_grid[i-1][0]
        for i in range(1,len(grid[0])):
            my_grid[0][i]=grid[0][i]+my_grid[0][i-1]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                my_grid[i][j]=min(my_grid[i-1][j],my_grid[i][j-1])+grid[i][j]
        return my_grid[-1][-1]

```
***
***
##### 67. Add Binary


```python
	# Edit By <font color=#0099ff>Python</font>

    #93%
    def addBinary(self, a: str, b: str) -> str:
    s = ""
    count = 0
    i = len(a) - 1
    j = len(b) - 1
    while count >= 1 or i >= 0 or j >= 0:
        count += int(a[i]) if i >= 0 else 0
        i -= 1
        count += int(b[j]) if j >= 0 else 0
        j -= 1
        s = str(int(count % 2)) + s
        count /= 2

    return s
    
```
***
***
##### 69. Sqrt(x)

```python
	# Edit By <font color=#0099ff>Python</font>

    #98%
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = int(left + (right - left) / 2)
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return mid
    
```
***
***
##### 70. Climbing Stairs


```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 83. Remove Duplicates from Sorted List

```python
	# Edit By <font color=#0099ff>Python</font>

    #99.98%
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
```
***
***
##### 100. Same Tree

```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 101. Symmetric Tree

```python
	# Edit By <font color=#0099ff>Python</font>

    def isSymmetric(root: TreeNode) -> bool:
        if root == None:
            return True
        return symmetric(root.left, root.right)


    def symmetric(leftNode: TreeNode, rightNode: TreeNode):
        if leftNode == None or rightNode == None:
            return leftNode==rightNode
        if leftNode.val != rightNode.val:
            return False
        return symmetric(leftNode.left, rightNode.right) and symmetric(leftNode.right, rightNode.left)


```
***
***
##### 104. Maximum Depth of Binary Tree

```python
	# Edit By <font color=#0099ff>Python</font>
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
***
##### 107. Binary Tree Level Order Traversal II


```python
	# Edit By <font color=#0099ff>Python</font>

    def levelOrderBottom(self,root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return list()
        a=[root]
        all=[]
        while len(a)!=0:
            length=len(a)
            cur=[]
            for i in range(length):
                temp=a[0]
                a.remove(temp)
                cur.append(temp.val)
                if temp.left != None:
                    a.append(temp.left)
                if temp.right != None:
                    a.append(temp.right)

            all.append(cur)

        return all[::-1]

```
***
***
##### 108. Convert Sorted Array To Binary Search Tree

```java
    public TreeNode sortedArrayToBST(int[] nums) {
            return sortedArrayToBST(nums, 0, nums.length);
        }
    
        public TreeNode sortedArrayToBST(int[] nums,int start, int end) {
            if(start == end) {
                return null;
            }
    
            int mid = start + (end - start) / 2;
            TreeNode root = new TreeNode(nums[mid]);
            root.left = sortedArrayToBST(nums, start, mid);
            root.right = sortedArrayToBST(nums, mid + 1, end);
    
            return root;
        }
```
***
***
##### 110. Balanced Binary Tree

```python
	# Edit By <font color=#0099ff>Python</font>
    #99.72%
    def isBalanced(root):
        if not root:
            return True
        node,count=balanced(root,0)
        return node
    
    def balanced(node: TreeNode, count: int):
        if not node:
            return True, count
        leftNode, left_dept = balanced(node.left, count)
        if not leftNode:
            return False, left_dept
        rightNode, right_dept = balanced(node.right, count)
        if not rightNode:
            return False, right_dept
        return abs(left_dept - right_dept) < 2,max(left_dept,right_dept)+1

```
***
***
##### 111. Minimum Depth of Binary Tree

```python
	# Edit By <font color=#0099ff>Python</font>

    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.min(root) + 1


    def min(self, root):
        if root.left == None and root.right == None:
            return 0
        elif root.left == None:
            return self.min(root.right) + 1
        elif root.right == None:
            return self.min(root.left) + 1
        else:
            return min(self.min(root.right), self.min(root.left)) + 1

```
***
***
##### 113. Path Sum II

```python
	# Edit By <font color=#0099ff>Python</font>

    #99%
    def pathSum(root: TreeNode, sum: int):
        all_list = []
        if not root:
            return list(all_list)
        suma(root, all_list, [], sum)
        return all_list
    
    
    def suma(node, all_list, this_list, sum):
        if not node:
            return
        if sum - node.val == 0 and not node.left and not node.right:
            this_list.append(node.val)
            all_list.append(this_list.copy())
            this_list.pop()
            return
        else:
            this_list.append(node.val)
            suma(node.left, all_list, this_list, sum - node.val)
            suma(node.right, all_list, this_list, sum - node.val)
            this_list.pop()
            return
    
```
***
***
##### 		118. Pascal's Triangle      
```java
        public List<List<Integer>> generate(int numRows) {
            List<List<Integer>> outList=new ArrayList<>();
            for(int i=0;i<numRows;i++){
                if(i==0)
                    outList.add(Arrays.asList(1));
                else if (i==1)
                    outList.add(Arrays.asList(1,1));
                else {
                    List<Integer> inList=new ArrayList<>();
                    inList.add(1);
                    for(int j=1;j<i;j++){
                        inList.add(outList.get(i-1).get(j-1)+outList.get(i-1).get(j));
                    }
                    inList.add(1);
                    outList.add(inList);
                }
    
            }
            return outList;
        }
```
***
***
##### 		119. Pascal's Triangle II  
```java
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre=new ArrayList<>();
        rowIndex++;
        if (rowIndex==1) {
            pre.add(1);
            return pre;
        }else if(rowIndex==2)
        {
            pre.add(1);
            pre.add(1);
            return pre;
        }else {
            pre.add(1);
            pre.add(1);
        }
        for (int i = 3; i <= rowIndex; i++) {
            List<Integer> cur=new ArrayList<>();

            for (int j = 0; j < i; j++) {
                if (j==0)
                    cur.add(1);
                else if (j==i-1){
                    cur.add(1);
                    pre=new ArrayList<>(cur);
                }else {
                    cur.add(pre.get(j-1)+pre.get(j));
                }
            }
        }
        return pre;
    }
```
***

***
##### 136. Single Number

```python
	# Edit By <font color=#0099ff>Python</font>
    def singleNumber(nums):
        return sum(set(nums))*2-sum(nums)
```
***
***
##### 	141. Linked List Cycle   
```java
    public boolean hasCycle(ListNode head) {
        ListNode fast=head,slow=head;
        while(fast!=null&&fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
            if(slow==fast)
                return true;
        }
        return false;
    }
```
***
***
##### 160. Intersection of two linkedlists

```java
    # Edit By <font color=#0099ff>Java</font>
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA==null||headB==null)
            return null;
        ListNode p1=headA,p2=headB;
        while(p1!=p2){
            p1=p1==null?headB:p1.next;
            p2=p2==null?headA:p2.next;
        }
        return p1;
    }
```
***
***
##### 171. Excel Sheet Column Number    
```java
    public int titleToNumber(String s) {
        if (s==null||s.length()==0)
            return 0;
        int length=1;
        int total=0;
        for (int i = s.length()-1; i >=0 ; i--,length*=26) {
            if (length==1)
                total+=s.charAt(i)-'A'+1;
            else {
                total+=(s.charAt(i)-'A'+1)*length;
            }
        }
        return total;
    }
```
***