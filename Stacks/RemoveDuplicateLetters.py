"""
Leetcode Link: https://leetcode.com/problems/remove-duplicate-letters/
"""

# Approach is to maintain visited dict and an array frequency counter/maintainer
class Solution:
    def removeDuplicateLetters(self, strr: str) -> str:
        if not strr: return None
        mapp = {}
        stack = []
        from collections import Counter
        counter = Counter(strr)
        
        for char in strr:
            if len(stack)==0:
                stack.append(char)
                counter[char]-=1
                mapp[char] = True
            else:
                if stack[-1]>char and char not in mapp:
                    while len(stack)>0 and stack[-1]>char and counter[stack[-1]]>0:
                        item = stack.pop()
                        mapp.pop(item)
                    stack.append(char)
                    counter[char]-=1
                    mapp[char] = True
                elif stack[-1]<char and char not in mapp:
                    stack.append(char)
                    counter[char]-=1
                    mapp[char] = True
                else:
                    counter[char]-=1
                    
        return ''.join(stack)