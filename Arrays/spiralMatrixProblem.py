"""
Leetcode: https://leetcode.com/problems/spiral-matrix/
Approach: Implementation problem with 2-d indexing.
"""

class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        if arr:
            res = []
            m,n = len(arr),len(arr[0])
            mid = (m+1)//2
            low = 0
            for i in range(mid):
                for j in range(low,n):
                    if len(res)<len(arr)*len(arr[0]):
                        res.append(arr[i][j])
                for j in range(low+1,m):
                    if len(res)<len(arr)*len(arr[0]):
                        res.append(arr[j][n-1])
                for j in range(n-2,low-1,-1):
                    if len(res)<len(arr)*len(arr[0]):
                        res.append(arr[m-1][j])
                for j in range(m-2,low,-1):
                    if len(res)<len(arr)*len(arr[0]):
                        res.append(arr[j][low])
                if len(res)==len(arr)*len(arr[0]):
                    break
                low+=1
                m-=1
                n-=1
            return res
        return arr