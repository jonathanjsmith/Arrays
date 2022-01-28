"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.
"""

import collections

def freqSort(nums):
    
    # use python Counter container
    # sort decreasing by value then increasing by frequency
    res = []
    c = collections.Counter(nums).most_common()
    c.sort(key=lambda x: x[0], reverse=True)
    c.sort(key=lambda x: x[1])
    
    for num, freq in c:
        res.extend([num] * freq)
    return res

"""
Time: O(n lgn)
Space: O(n)
"""

nums = [1,1,2,2,2,3]
ans = freqSort(nums)
print(ans)