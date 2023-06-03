import enum
from typing import List

## ATTEMPT 1
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = 0
#         max_price = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[i] < prices[j] and (prices[j] - prices[i]) > (max_price-min_price):
#                     min_price = prices[i]
#                     max_price = prices[j]
#         diff = max_price - min_price
#         if diff > 0:
#             return diff
#         else:
#             return 0

## ATTEMPT 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = {}
        for index, price in enumerate(prices):
            prices[index] = price
        # filter dictionary out for any subsequent duplicate values. No need to check anything other than the first one
        # and the dictionary will preserve the order. 
        min_price = 0
        max_price = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j] and (prices[j] - prices[i]) > (max_price-min_price):
                    min_price = prices[i]
                    max_price = prices[j]
        diff = max_price - min_price
        if diff > 0:
            return diff
        else:
            return 0
test = Solution()
# print(test.maxProfit([7,6,4,3,1]), ' should be 0')
# print(test.maxProfit([7,1,5,3,6,4]), ' should be 5')
