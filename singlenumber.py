"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

def singleNumber(nums):
    
    res = nums[0]
    
    # take the XOR of each int in the array
    # the leftover bits will be the single number
    for i in range(1, len(nums)):
        res ^= nums[i]
        
    return res

"""
Time: O(n)
Space: O(1)
"""

input_1 = [4, 1, 2, 1, 2]

ans = singleNumber(input_1)
print(ans)