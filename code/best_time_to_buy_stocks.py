class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lpointer, wpointer, maxProfit = 0, 1, 0
        while (wpointer<len(prices)):
            if (prices[wpointer]-prices[lpointer]>maxProfit):
                maxProfit = prices[wpointer]-prices[lpointer]
            if (prices[lpointer]>prices[wpointer]):
                lpointer = wpointer
                # wpointer = wpointer + 1
            wpointer = wpointer + 1
        return maxProfit