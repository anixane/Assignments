"""
Leetcode: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, strr: str) -> bool:
        """
        Logic: Simple stack question
        """
        stack = []
        for char in strr:
            if len(stack)==0:
                stack.append(char)
            elif (char=='}' and stack[-1]=='{') or (char==']' and stack[-1]=='[') or (char==')' and stack[-1]=='('):
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True