"""
https://leetcode.com/problems/missing-ranges/submissions/
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number isin one of the ranges.
"""

def findMissingRanges(nums, lower, upper):
    nums = [lower-1] + nums + [upper + 1]
    ranges = []
    
    # check for differences between each num and append ranges
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 2:
            ranges.append(str(nums[i]+1))
        elif nums[i+1] - nums[i] > 2:
            ranges.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
    return ranges

"""
Time: O(n)
Space: O(1)
"""

input_1 = [0,1,3,50,75]
lower = 0
upper = 100

ans = findMissingRanges(input_1, 0, 100)
print(ans)