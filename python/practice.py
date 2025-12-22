#backtracking combination:
def backtracking(start):
    if meet_condtion:
        res.append(path.copy())
    for i in range(start,n+1):
        path.append(i)
        backtracking(i+1)
        path.pop()

def permute(nums):
    res = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            #if already used 
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])

            backtracking()

            path.pop()
            used[i] = False

    backtrack()
    return 



from collections import deque,defaultdict,Counter
import heapq
import biscet import bisect_left,bisect_right
import bisect import bisect_left,bisect_right


q = deque([start])
q.append(x)
x= q.popleft()

q = deque([start])
seen = {start}/visited
step=0
while q:
    len = len(queue)
    for i in range(len):
        cur = q.popleft()
        #process cur

        for nei in neighbour(cur):
            if nei in seen:
                continue
            seen.add(nei)
            queue.append(nei)

    step += 1