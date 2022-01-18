"""
https://leetcode.com/problems/can-place-flowers/
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""

def canPlaceFlowers(flowerbed, n):
    # iterate through flowerbed and place flowers
    for i, flower in enumerate(flowerbed):
        if i == 0 or not flowerbed[i-1]:
            if i == len(flowerbed)-1 or not flowerbed[i+1]:
                if not flower:
                    flowerbed[i] = 1
                    n -= 1
    return n <= 0

"""
Time: O(n)
Space: O(1)
"""

flowerbed = [1,0,0,0,1]
n = 1
ans = canPlaceFlowers(flowerbed, n)
print(ans)

flowerbed = [1,0,0,0,1]
n = 2
ans = canPlaceFlowers(flowerbed, n)
print(ans)