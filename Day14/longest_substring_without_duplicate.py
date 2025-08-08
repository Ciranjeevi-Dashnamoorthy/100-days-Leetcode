class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        max_length=0
        left=0
        string=""

        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[left])
                left+=1
            a.add(s[i])
            max_length=max(max_length,len(a))

        return max_length

                
