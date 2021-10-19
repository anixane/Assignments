"""
Heaps in Python
"""

from heapq import heapify, heappush,heappop
arr = [34,23,1,56]
print(arr)
heapify(arr) #By default, it builds a min-heap, min on top

#Adding items in above min-heap
heappush(arr,25)
while arr:
    print(heappop(arr))
    
arr = [1,2,3,4,5]   
    
"""
Max-heap in python
"""
# Use lambda function to multiply whole arr with -1
arr = list(map(lambda x:x*-1,arr))
heapify(arr)
# popping elements from max-heap
while arr:
    print(heappop(arr)*-1)
