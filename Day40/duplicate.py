class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter

        freq=Counter(s)
        seen=set()
        stack=[]

        for i in range(len(s)):
            freq[s[i]]-=1
            if s[i] in seen:
                continue

            while stack and s[i]<stack[-1] and freq[stack[-1]]>0 :
                
                seen.remove(stack.pop())

            stack.append(s[i])
            seen.add(s[i])
            print(stack)
        return "".join(stack)