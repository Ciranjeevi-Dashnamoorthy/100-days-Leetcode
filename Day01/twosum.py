class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=set()
        for i in range(len(nums)):
         compli=target-nums[i]
         if compli in num:
            return [i,nums.index(compli)]
         num.add(nums[i])
