"""
https://leetcode.com/problems/sequential-digits/submissions/
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""

def sequentialDigits(low, high):
    
    sample = "123456789"
    nums = []
    for length in range(len(str(low)), len(str(high))+1):
        for start in range(10-length):
            num = int(sample[start:start+length])
            if low <= num <= high:
                nums.append(num)
                
    return nums

"""
Time: O(1)
Space: O(1)
"""

low = 100
high = 300
ans = sequentialDigits(low, high)
print(ans)

low = 1000
high = 13000
ans = sequentialDigits(low, high)
print(ans)