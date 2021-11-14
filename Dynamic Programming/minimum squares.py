"""
Problem: Mapp it to coin change problem
"""
class Solution:
	def MinSquares(self, n):
	    import math
		squares = [i**2 for i in range(1,int(math.sqrt(n)))]
		from collections import defaultdict
		mapp = defaultdict(int)
		def getMin(squares,n):
		    nonlocal mapp
		    if n==0: return 0
		    if n<0: return float('inf')
		    if n in mapp: return mapp[n]
		    res = []
		    for sq in squares:
		        res.append(getMin(squares,n-sq))
		    mapp[n]=min(res)+1
		    return mapp[n]
	    res = getMin(squares,n)
	    return res if res!=float('inf') else -1
