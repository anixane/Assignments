"""
Problem: https://eugenejw.github.io/2017/07/leetcode-582
Logic: create simple hashmapp of key:list and apply simple dfs (recursive)
"""
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5

from collections import defaultdict
mapp = defaultdict(list)
for i in range(len(pid)):
    mapp[ppid[i]].append(pid[i])
print(mapp)

res = []
def dfs(kill):
    res.append(kill)
    if kill in mapp:
        for item in mapp[kill]:
            dfs(item)

dfs(kill)
print(res)
