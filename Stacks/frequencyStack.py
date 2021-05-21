"""
Leetcode: https://leetcode.com/problems/maximum-frequency-stack/

Approach: Idea is to maintain a counter hashmap and a hashmanp of lists (stacks)
"""

class frequencyStack():
    def __init__(self):
        from collections import defaultdict
        self.counter = defaultdict(int)
        self.stackBucket = defaultdict(list)
        self.maxFrequencySoFar = 0
    
    def push(self,item):
        self.counter[item]+=1
        count = self.counter[item]
        #pushing it to stack bucket as well
        self.stackBucket[count].append(item)
        self.maxFrequencySoFar = max(count, self.maxFrequencySoFar)

    def pop(self):
        if self.maxFrequencySoFar==0:
            return "Stack bucket is empty."
        #popping the element from max-frequency stack of stack-bucket
        item = self.stackBucket[self.maxFrequencySoFar].pop()
        #update the counter
        self.counter[item]-=1
        #update the maxFrequencySoFar
        if len(self.stackBucket[self.maxFrequencySoFar])==0:
            self.maxFrequencySoFar-=1
        return item

obj = frequencyStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())