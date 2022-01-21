"""
https://leetcode.com/problems/koko-eating-bananas/
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import math

def minSpeed(piles, h):
    
    # use binary search to test each speed of eating
    lo, hi = 1, max(piles)
    
    while lo < hi:
        mid = (lo + hi) >> 1
        if sum(math.ceil(pile / mid) for pile in piles) > h:
            lo = mid + 1
        else:
            hi = mid
            
    return lo

"""
Time: O(n lg(m)) where m is the maximum number of bananas in a pile
Space: O(1)
"""

piles = [3,6,7,11]
h = 8
ans = minSpeed(piles, h)
print(ans)

piles = [30,11,23,4,20]
h = 5
ans = minSpeed(piles, h)
print(ans)

piles = [30,11,23,4,20]
h = 6
ans = minSpeed(piles, h)
print(ans)