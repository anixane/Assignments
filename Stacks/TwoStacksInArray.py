"""
Problem: Implement 2 stacks in an array.

Approach 1: Divide the array equally in 2 halves and perform operations.
Drawback: its not space optimized.

Approach 2: lets use both the end of array as 2 diffent stacks.
Advantage: Its space optimized.
"""

class TwoStacksInArray():
    def __init__(self,n):
        self.capacity = n
        self.stack = [None]*n
        self.top1 = -1
        self.top2 = n

    def push(self,stackNumber,item):
        if self.top1 < self.top2-1:
            if stackNumber==1:
                #increment top1 and insert the element
                self.top1+=1
                self.stack[self.top1] = item

            else:
                #decrement top2 and insert the element
                self.top2-=1
                self.stack[self.top2] = item
        else:
            print("No space in stack")
            return

    def pop(self,stackNumber):
        if stackNumber==1:
            if self.top1>=0:
                item = self.stack[self.top1]
                self.top1-=1
                return item
        else:
            if self.top2<self.capacity:
                item = self.stack[self.top2]
                self.top2+=1
                return item
        print("Item cannot be popped from stack number {0}".format(stackNumber))
        return

stack = TwoStacksInArray(5)
stack.push(1,5)
stack.push(2,10)
stack.push(2,15)
stack.push(1,11)
stack.push(2,7)

print(stack.pop(1))
print(stack.pop(2))