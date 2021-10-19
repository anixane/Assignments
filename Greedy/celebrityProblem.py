"""
Problem: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/
"""

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        indegree, outdegree = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    indegree[j]+=1
                    outdegree[i]+=1
                    
        for i in range(n):
            if outdegree[i]==0 and indegree[i]==n-1:
                return i
        return -1
