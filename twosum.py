"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def twoSum(nums, target):
    
    # create hash map of complements to keep track
    complements = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in complements:
            return [complements[nums[i]], i]
        complements[target - nums[i]] = i
    
    return []

"""
Time: O(n)
Space: O(n)
"""

nums = [2,7,11,15]
target = 9
ans = twoSum(nums, target)
print(ans)