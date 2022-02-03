"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
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