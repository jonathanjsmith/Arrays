"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to the closest person.
"""

def maxDistance(seats):
    # case 1: front seat, case 2: middle seat, case 3: end seat
    prev, res = -1, 0
    for i, seat in enumerate(seats):
        if seat:
            res = max(res, i if prev < 0 else (i - prev) // 2)
            prev = i
    return max(res, len(seats)-1-prev)

"""
Time: O(n)
Space: O(1)
"""

seats = [1,0,0,0,1,0,1]
ans = maxDistance(seats)
print(ans)

seats = [1,0,0,0]
ans = maxDistance(seats)
print(ans)


