class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0 or s[0]=="0":
            return 0
        
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            single=int(s[i-1])
            double=int(s[i-2:i])

            if single!=0:
                dp[i]+=dp[i-1]
            if 10<=double<=s26:
                dp[i]+=dp[i-2]
        return dp[n]
        