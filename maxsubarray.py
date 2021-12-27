"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""

def maxSubarray(nums):
    
    t = 0
    maxsum = 0
    
    for i in range(len(nums)):
        # add num to running max and calc new max
        t += nums[i]
        maxsum = max(maxsum, t)
        
        # if running max is negative, restart
        if t < 0:
            t = 0
            
    return maxsum

"""
Time: O(n)
Space: O(1)
"""

input_1 = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxSubarray(input_1)
print(ans)
