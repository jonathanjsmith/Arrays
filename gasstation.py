"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

def startingStation(gas, cost):
    
    total_tank, curr_tank = 0, 0
    start = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
            
    return start if total_tank >= 0 else -1

"""
Time: O(n)
Space: O(1)
"""

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
ans = startingStation(gas, cost)
print(ans)

gas = [2,3,4]
cost = [3,4,3]
ans = startingStation(gas, cost)
print(ans)