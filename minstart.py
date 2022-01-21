"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

def minStart(nums):
    
    min_sum = total = 0
    
    # find minimum value in nums
    # find minimum of total in nums
    for num in nums:
        total += num
        min_sum = min(min_sum, total)
    
    # return minimum value needed to always be greater than 1
    return -min_sum + 1

"""
Time: O(n)
Space: O(1)
"""

nums = [-3,2,-3,4,2]
ans = minStart(nums)
print(ans)

nums = [1,2]
ans = minStart(nums)
print(ans)