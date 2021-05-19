"""
Leetcode: https://leetcode.com/problems/validate-stack-sequences/

Logic: Idea is to keep pushing the elements to a stack from "pushed" array and as you find same value at pushed and poped, pop the stack and move ahead in the poped array comparing stack content. 
In the end stack should be empty.
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        def isEmpty(stack):
            return len(stack)==0
        
        #edge case when both stacks are empty
        if not pushed and not popped: return True
        lenn = len(pushed)
        stack = []
        i,j = 0,0
        while i<lenn:
            if pushed[i]==popped[j]:
                j+=1
                #now check for other remaining elements in our stack and check if its in popped[j] as well
                while not isEmpty(stack) and stack[-1]==popped[j]:
                    stack.pop()
                    j+=1
            else:
                stack.append(pushed[i])
            i+=1
            
        #now checking for remaining elements in pushed stack, whether it matches the popped stack order
        while not isEmpty(stack):
            if stack[-1]==popped[j]:
                j+=1
                stack.pop()
            else:
                return False
        
        #at last we have to check whether our stack is empty or not, if it is, that means that sequence is possible
        return isEmpty(stack)