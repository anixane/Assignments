#gfg practice --> edge case different than fibonacci number
class Solution:
    def __init__(self):
        from collections import defaultdict
        self.mapp = defaultdict(int)
        self.mapp[1] = 1
        self.mapp[2] = 2
        
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        if n in self.mapp: return self.mapp[n]
        res = (self.countWays(n-1)+self.countWays(n-2))%1000000007
        self.mapp[n]=res
        return res
