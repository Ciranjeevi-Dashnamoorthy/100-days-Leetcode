class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
          prefixsumcount = {0: 1}
          prefixsum = 0
          count = 0

          for num in nums:
           prefixsum += num
           if prefixsum - k in prefixsumcount:
             count += prefixsumcount[prefixsum - k]
           prefixsumcount[prefixsum] = prefixsumcount.get(prefixsum, 0) + 1

          return count
