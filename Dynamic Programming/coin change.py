"""
Problem: https://leetcode.com/problems/coin-change/
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import defaultdict
        mapp = defaultdict(int)
        def getCoin(coins, amount):
            nonlocal mapp
            res = []
            if amount==0: return 0
            if amount<0: return float('inf')
            if amount in mapp: return mapp[amount]
            for coin in coins:
                res.append(getCoin(coins,amount-coin))
            mapp[amount] = min(res)+1
            return mapp[amount]
            
        res = getCoin(coins, amount)
        return res if res!=float('inf') else -1 
            
