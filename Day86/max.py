class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[0]*n
        dp2=[0]*n
        dp1[0],dp2[0]=nums[0],nums[0]
        for i in range(1,n):
            dp1[i]=max(nums[i],dp1[i-1]*nums[i],dp2[i-1]*nums[i])
            dp2[i]=min(nums[i],dp1[i-1]*nums[i],dp2[i-1]*nums[i])

        return max(dp1)
        