"""
Problem: https://leetcode.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        REF: https://leetcode.com/problems/decode-ways/discuss/1546849/Python-DP-solution-with-notes-and-diagram
        Important : Handle case having 0
        """
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        if  s[0] == '0':
            return 0
        else:
            dp[1] = 1
        for i in range(2,len(s)+1):
            if s[i-1] == "0": #i-1 is actually pointing the ith index of s string
                if s[i-2] == "1" or s[i-2] == "2":
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if s[i-2] == '1' or s[i-2] == '2' and int(s[i-1]) < 7:
                    #add the decoded ways i have till that
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[len(s)]
