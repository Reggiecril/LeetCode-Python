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

