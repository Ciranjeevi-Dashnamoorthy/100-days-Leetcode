from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        k=len(p)
        res=[]
        check=Counter(p)
        window=Counter(s[:k])
        if window==check:
            res.append(0)

        for i in range(k,n):
            window[s[i]]+=1
            window[s[i-k]]-=1

            if window==check:
                res.append(i-k+1)

          
        return res


        