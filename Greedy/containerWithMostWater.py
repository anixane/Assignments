"""
Problem: https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer problem. Typical.
        """
        left,right,maxxArea = 0, len(height)-1, 0
        while left<right:
            horizontalDistance, minHeight = right-left, min(height[left],height[right])
            maxxArea = max(maxxArea,horizontalDistance*minHeight)
            if height[left]<height[right]: left+=1
            else: right-=1
        return maxxArea
