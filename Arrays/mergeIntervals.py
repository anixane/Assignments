"""
Leetcode: https://leetcode.com/problems/merge-intervals/

Approach: sorting based on 1st element is a must.
Afterwards, apply the general logic.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        if len(intervals)==1: return intervals
        else:
            intervals.sort()
            prev_start,prev_end = intervals[0]
            res = []
            for i in range(1,len(intervals)):
                curr_start,curr_end = intervals[i]
                if curr_start>prev_end:
                    res.append([prev_start,prev_end])
                    prev_start,prev_end = curr_start,curr_end
                else:
                    prev_start = min(prev_start,curr_start)
                    prev_end = max(prev_end,curr_end)
            res.append([prev_start,prev_end])
            return res
