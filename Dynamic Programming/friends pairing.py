"""
Problem: https://practice.geeksforgeeks.org/problems/friends-pairing-problem5425/
"""

class Solution:
    def countFriendsPairings(self, n):
        """
        Intution:
        total no of ways = no. of ways new guy can go alone + no. of ways when new guy forms a pair with anyone in remining friends
        f(n) = f(n-1) + (n-1)*f(n-2)
        //f(n-2) because 1 friend is gonna be in pair with nth friend (new guy)
        """
        from collections import defaultdict
        mapp = defaultdict(int)
        mapp[1], mapp[2] = 1,2
        def ways(n):
            nonlocal mapp
            if n in mapp: return mapp[n]
            res = (ways(n-1)+((n-1)*ways(n-2)))%1000000007
            mapp[n] = res
            return mapp[n]
        return ways(n)
