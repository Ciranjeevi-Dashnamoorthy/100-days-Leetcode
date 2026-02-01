class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n=len(nums)
        m0=[]
        m1=[]
        m2=[]
        for i in range(n):
            if nums[i]%3==0:
                m0.append(nums[i])
            elif nums[i]%3==1:
                m1.append(nums[i])
            elif nums[i]%3==2:
                m2.append(nums[i])
        m0.sort(reverse=True)
        m1.sort(reverse=True)
        m2.sort(reverse=True)
        ans=0
        if len(m0)>=3:
            ans=max(ans,sum(m0[:3]))

        if len(m1)>=3:
            ans=max(ans,sum(m1[:3]))
        if len(m2)>=3:
            ans=max(ans,sum(m2[:3]))

        if len(m0)>=1 and len(m1)>=1 and len(m2)>=1:
            ans=max(ans,m0[0]+m1[0]+m2[0])
        return ans
        
        
        
        
                