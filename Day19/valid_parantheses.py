class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}

        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            else:
                if stack and stack[-1]==mapping[s[i]]:
                    stack.pop()
                else:
                    return False
        print(stack)
        return not stack
