# 322. Coin Change
# Solved
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # greedy not working
        # coins = sorted(coins)
        # residual = amount % coins[len(coins) -1] 
        # total = amount // coins[len(coins) -1] 
        # if len(coins) == 1 and amount == 0:
        #     return 0
        # if len(coins) == 1 and amount % coins[0] != 0:
        #     return -1
        # if len(coins) == 1 and amount % coins[0] == 0:
        #     return amount // coins[0]
        # elif len(coins) == 0:
        #     reeturn -1
        # for each in range(len(coins)-2,-1,-1): 
        #     if coins[each] <= residual and residual != 0:
        #         total += residual // coins[each]
        #         residual = residual % coins[each] 
        #     if residual == 0:
        #         return total
        # return -1
class Solution(object):

    def coinChange(self,coins, amount):
    # Create an array to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins needed to make up amount 0
        dp[0] = 0
        
        # Iterate through each coin denomination
        for coin in coins:
            # Update the dp array for each amount from the current coin to the target amount
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Check if the final entry in dp is still the initial value (infinity)
        # If so, it means the amount cannot be made up by any combination of coins
        return dp[amount] if dp[amount] != float('inf') else -1



        

            

        
