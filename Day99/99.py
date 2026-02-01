class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        if k>n//2:
            profit=0
            for i in range(n-1):
                if prices[i+1]-prices[i]>0:
                    profit+=prices[i+1]-prices[i] 
            return profit
        dp=[[0]*n for _ in range(k+1)]
        for t in range(1,k+1):
            diff=-prices[0]
            for i in range(1,n):
                dp[t][i]=max(dp[t][i-1],prices[i]+diff)
                diff=max(diff,dp[t-1][i]-prices[i])
        return dp[t][n-1]