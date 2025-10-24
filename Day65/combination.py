class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(index,path,curr):
            if curr==target:
                res.append(path.copy())
                return
            if curr>target or index>=(len(candidates)):
                return
            path.append(candidates[index])
            backtrack(index,path,curr+candidates[index])
            path.pop()
            backtrack(index+1,path,curr)

        backtrack(0,[],0)
        return res

        