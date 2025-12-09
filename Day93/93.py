class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        n=len(height)
        arrmin=[0]*n
        arrmin[0]=height[0]
        arrmax=[0]*n
        arrmax[-1]=height[-1]
        arr=[0]*n
        for i in range(1,n):
            arrmin[i]=max(arrmin[i-1],height[i])
        for j in range(n-2,-1,-1):
            arrmax[j]=max(arrmax[j+1],height[j])
            
        for i in range(n):
            area+=min(arrmin[i],arrmax[i])-height[i]
        return area
        