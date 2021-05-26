"""
Leetcode: https://leetcode.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Approach 1: Includes simple triple reversing
        """
        if not arr or len(arr)==1: return arr
        def reverse(arr,low,high):
            while low<high:
                arr[low],arr[high] = arr[high],arr[low]
                low+=1
                high-=1
        
        n = len(arr)
        k = k%n #because k can be greater than n, it will avoid excessive processing
        #step1: reverse the entire list
        reverse(arr,0,n-1)
        #step2: reverse first k elements
        reverse(arr,0,k-1)
        #step3: reverse remaining elements after k
        reverse(arr,k,n-1)
        
        """
        Approach 2: Using pop and pushleft operation of deque k%n times
        """
        deq = deque(nums)
        k = k%len(arr)
        while k > 0:
            right = deq.pop()
            deq.appendleft(right)
            k -= 1
        
        for i in range(len(arr)):
            nums[i] = deq[i]
