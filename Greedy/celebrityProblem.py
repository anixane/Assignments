"""
Problem: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/
"""

#TC: O(n-square), SC: O(n)
class Solution:
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

################ OPTIMIZED CODE ##################################
    
    
#TC: O(n), SC: O(1)  
class Solution:
    def celebrity(self, M, n):
        """
        Optimization: O(n)
        """
        celeb = 0
        for i in range(n):
            if M[celeb][i]==1:
                celeb=i
        #verify
        for i in range(n):
            if i!=celeb:
                if M[celeb][i]==1 or M[i][celeb]==0:
                    return -1
        return celeb
