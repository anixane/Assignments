class Solution:
    def trap(self, height: List[int]) -> int:
        #using prefix and postfix arrays for local maximas
        def getTrappedWater(heights):
            if not heights: return 0
            left, right = [],[]
            maxx = float('-inf')
            for height in heights:
                maxx = max(maxx,height)
                left.append(maxx)
            maxx = float('-inf')
            for i in range(len(heights)-1,-1,-1):
                maxx = max(maxx,heights[i])
                right.append(maxx)
            right.reverse()
            
            #boundary buildings have no water over it, so we can skip those in loop for calculating ans
            result = 0
            for i in range(1,len(heights)-1):
                result+=(min(left[i],right[i])-heights[i])
            return result
        
        return getTrappedWater(height)
        