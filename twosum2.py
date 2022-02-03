"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

def twoSum(numbers, target):
    
    l, r = 0, len(numbers)-1
    while l < r:
        twoSum = numbers[l] + numbers[r]
        if twoSum == target:
            return [l+1, r+1]
        elif twoSum > target:
            r -= 1
        else:
            l += 1
    return []

"""
Time: O(n)
Space: O(1)
"""

numbers = [2,7,11,15]
target = 9
ans = twoSum(numbers, target)
print(ans)