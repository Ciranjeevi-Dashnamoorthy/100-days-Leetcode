class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        total=m+n
        half=(total+1)//2

        l,r=0,m

        while l<=r:
            i=(l+r)//2
            j=half-i

            leftA=nums1[i-1] if i>0 else float("-inf")
            rightA=nums1[i] if i<m else float("inf")
            leftB=nums2[j-1] if j>0 else float("-inf")
            rightB=nums2[j] if j<n else float("inf")

            if leftA<=rightB and leftB<=rightA: 
                if total%2==0:
                    return float((max(leftA,leftB)+min(rightA,rightB))/2)
                else:
                    return max(leftA,leftB)
            elif leftA>rightB:
                r=i-1
            else:
                l=i+1
        return -1
         
        