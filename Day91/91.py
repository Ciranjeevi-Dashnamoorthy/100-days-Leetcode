class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import heapq
        heap=[]
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))
        
        res=[""]*len(score)
        rank=1
        while heap:
            s,index=heapq.heappop(heap)
            if rank==1:
                res[index]="Gold Medal"
            elif rank==2:
                res[index]="Silver Medal"
            elif rank==3:
                res[index]="Bronze Medal"
            else:
                res[index]=str(rank)
            rank+=1
        return res