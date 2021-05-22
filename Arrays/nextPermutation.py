"""
Leetcode: https://leetcode.com/problems/next-permutation/

Approach: Can be divided in 3 basic steps.
1. starting from back of the array, find the element which breaks the strictly increasing order.
Set a pointer on that index.
2. from the back of the array till the index of identified element, find the element which is just greater than the element identified in step 1.
3. Swap the elements identified in step 1 and step 2.
4. reverse the elements from index i+1 till end of array. 
Considering i = index of element identified in step 1.
"""


class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if arr == sorted(arr,reverse = True):
            arr.sort()
            return
        else:
            i,j = 0,0
            for i in range(len(arr)-1,0,-1):
                if arr[i-1]<arr[i]:
                    i -= 1
                    break
            for j in range(len(arr)-1,i,-1):
                if arr[j]>arr[i]:
                    break
            arr[i],arr[j] = arr[j],arr[i]
            temp = arr[i+1:]
            temp.reverse()
            
            j = 0
            for k in range(i+1,len(arr)):
                arr[k] = temp[j]
                j+=1