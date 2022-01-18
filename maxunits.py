"""
https://leetcode.com/problems/maximum-units-on-a-truck/submissions/
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    * numberOfBoxesi is the number of boxes of type i.
    * numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
"""

def maxUnits(boxTypes, truckSize):
    total = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    for boxes, units in boxTypes:
        boxes = min(boxes, truckSize)
        total += boxes*units
        truckSize -= boxes
        if truckSize == 0:
            break
    return total

"""
Time: O(nlg(n))
Space: O(1)
"""

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
ans = maxUnits(boxTypes, truckSize)
print(ans)

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
ans = maxUnits(boxTypes, truckSize)
print(ans)