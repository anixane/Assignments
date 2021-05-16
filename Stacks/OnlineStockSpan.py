"""
Leetcode Link: https://leetcode.com/problems/online-stock-span/
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 0
        
    def isEmpty(self):
        if self.stack:
            return False
        return True
        

    def next(self, price: int) -> int:
        while True:
            if self.isEmpty():
                self.stack.append([self.index,price])
                self.index+=1
                return self.index
            else: 
                current = self.stack[-1]
                if current[1]<=price:
                    self.stack.pop()
                else:
                    res =  self.index-current[0]
                    self.stack.append([self.index,price])
                    self.index+=1
                    return res