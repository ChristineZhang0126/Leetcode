# 121. Best Time to Buy and Sell Stock
# Easy
# 29.5K
# 1K
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # brute force
        # max_profit = 0
        # for i in range(len(prices)):
        #     for index in range(i + 1, len(prices)):
        #         if prices[index] > prices[i] and (prices[index] - prices[i]) > max_profit:
        #             max_profit = prices[index] - prices[i]
        # return max_profit

        # two pointer
        l = 0
        r = 1
        max_pro = 0
        while l  < r and r < len(prices):
            if prices[l] < prices[r]:
                if (prices[r] - prices[l]) > max_pro:
                    max_pro = prices[r] - prices[l]
            else:
                l = r
            r +=1
        return max_pro

# solution two:
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices or len(prices) == 1:
#             return 0

#         # Initialize variables
#         min_price = prices[0]
#         max_profit = 0

#         # Iterate through the prices
#         for price in prices[1:]:
#             # Update the minimum price
#             min_price = min(min_price, price)
            
#             # Update the maximum profit
#             max_profit = max(max_profit, price - min_price)

#         return max_profit
