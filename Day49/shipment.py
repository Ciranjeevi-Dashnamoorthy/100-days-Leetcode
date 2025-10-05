class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap):
            current=0
            days_count=1
            for w in weights:
                if current +w>cap:
                    days_count+=1
                    current=0
                current+=w
            return days_count<=days
        l,r=max(weights),sum(weights)
        while l<r:
            mid=(l+r)//2
            if possible(mid):
                r=mid
            else:
                l=mid+1
        return r
        