"""
Problem: https://leetcode.com/problems/k-closest-points-to-origin/
Paradigm: Simple min-heap application
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heapify,heappop,heappush
        import math
        heap = []
        heapify(heap)
        for point in points:
            x,y = point[0],point[1]
            sq = math.sqrt(x**2+y**2)
            heappush(heap,[sq,x,y])
        res = []
        while k>0:
            item = heappop(heap)
            res.append([item[1],item[2]])
            k-=1
        return res
