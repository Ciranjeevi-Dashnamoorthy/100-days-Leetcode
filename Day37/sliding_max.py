class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        l,r=0,0
        queue=deque()
        result=[]

        while r<len(nums):
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)

            if l>queue[0]:
                queue.popleft()
            
            if (r+1)>=k:
                result.append(nums[queue[0]])
                l+=1
            r+=1
        return result
                