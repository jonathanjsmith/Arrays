"""
https://leetcode.com/problems/plus-one/
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

def plusOne(digits):
    
    # loop through list backwards, incrementing index
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # if digit is 9, increment and carry the one
        digits[i] = 0
    
    # if the first index of list overflowed, add to the list
    return [1] + digits

"""
Time: O(n)
Space: O(1)
"""

input_1 = [1,2,3]
input_2 = [9,9,9]

ans1 = plusOne(input_1)
ans2 = plusOne(input_2)

print(ans1)
print(ans2)
        