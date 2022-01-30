"""
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

def reverse(nums, i, j):
    # swap integers until pointers reach middle of array
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def rotate(nums, k):
    
    # swap both sides of array at pivot, then reverse entire array
    k %= len(nums)
    reverse(nums, 0, len(nums)-1-k)
    reverse(nums, len(nums)-k, len(nums)-1)
    reverse(nums, 0, len(nums)-1)
    
"""
Time: O(n)
Space: O(1)
"""

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)