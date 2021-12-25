"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfit(prices):
    
    # minimum profit is 0
    profit = 0
    minimum = prices[0]
    
    for i in range(1, len(prices)):
        # find lowest value in list up to current iteration
        if prices[i] < minimum:
            minimum = prices[i]
        # compare each price to lowest value
        elif prices[i] - minimum > profit:
            profit = prices[i] - minimum
            
    return profit

"""
Time: O(n)

Space: O(1)

"""

input_1 = [7,1,5,3,6,4]
input_2 = [7,6,4,3,1]

output_1 = maxProfit(input_1)
output_2 = maxProfit(input_2)

print(output_1)
print(output_2)
