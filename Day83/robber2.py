class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def dp(arr): 
         if len(arr)==1:
            return arr[0] 
         dp=[0]*len(arr)
         dp[0]=arr[0]
         dp[1]=max(arr[1],arr[0])
        
         for i in range(2,len(arr)):
            dp[i]=max(dp[i-2]+arr[i],dp[i-1])
         return dp[-1]
        
        run1=dp(nums[:-1])
        run2=dp(nums[1:])
        return max(run1,run2)
