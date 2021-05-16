class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: we just need to focus on water over a particular bar.
        This boils down to the problem of knowing local maxima on both sides of the bar.
        """
        #using prefix and postfix arrays for local maximas
        def getTrappedWater(heights):
            if not heights: return 0
            left, right = [],[]
            maxx = float('-inf')
            for height in heights:
                maxx = max(maxx,height)
                left.append(maxx)
                
            #re-initialize maxx variable for traversing list in reverse dxn
            maxx = float('-inf')
            for i in range(len(heights)-1,-1,-1):
                maxx = max(maxx,heights[i])
                right.append(maxx)
            
            #reversing for makng the order correct.
            right.reverse()
            
            #boundary buildings have no water over it, so we can skip those in loop for calculating ans
            result = 0
            for i in range(1,len(heights)-1):
                result+=(min(left[i],right[i])-heights[i])
            return result
        
        def twoPointerApproach(heights):
            if not heights: return 0
            result = 0
            left,right = 0,len(heights)-1
            l_max,r_max = heights[left],heights[right]
            while left<right:
                if heights[left]<heights[right]:
                    if heights[left]>l_max:
                        #just update the left-max
                        l_max = heights[left]
                    else:
                        result+=(l_max-heights[left])
                    left+=1
                else:
                    if heights[right]>r_max:
                        #update right max
                        r_max = heights[right]
                    else:
                        result+=(r_max-heights[right])
                    right-=1
            return result
        
        return twoPointerApproach(height)
        