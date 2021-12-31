"""
https://leetcode.com/problems/binary-search/submissions/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""

def binarySearch(nums, target):
    
    low, high = 0, len(nums)-1
    
    # determine whether target is to the left or right of midpoint
    # move bounds accordingly
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    
    return -1

"""
Time: O(lg n)
Space: O(1)
"""

input_1 = [-1,0,3,5,9,12]

ans1 = binarySearch(input_1, 9)
ans2 = binarySearch(input_1, 2)

print(ans1)
print(ans2)
