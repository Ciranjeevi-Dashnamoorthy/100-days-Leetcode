class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def palindrome(k):
            return k == k[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])  
                return

            for end in range(start + 1, len(s) + 1):
                curr = s[start:end]
                if palindrome(curr):
                    path.append(curr)           
                    backtrack(end, path)      
                    path.pop()                

        backtrack(0, [])
        return res


        