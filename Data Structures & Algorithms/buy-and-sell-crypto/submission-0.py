class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[j] > prices[i]:
                j = i
            elif prices[j] < prices[i]:
                profit = max(profit, prices[i]-prices[j])
                
            print(profit)
        return profit if profit > 0 else 0
        
        