"""
https://leetcode.com/problems/meeting-rooms/
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""

def canAttend(intervals):
    
    # sort all intervals
    intervals.sort()
    
    for i in range(len(intervals)-1):
        if intervals[i+1][0] < intervals[i][1]:
            return False
    
    return True

"""
Time: O(n lg(n))
Space: O(1)
"""

intervals = [[0,30],[5,10],[15,20]]
ans = canAttend(intervals)
print(ans)

intervals = [[7,10],[2,4]]
ans = canAttend(intervals)
print(ans)