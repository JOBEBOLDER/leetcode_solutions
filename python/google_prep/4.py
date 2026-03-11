'''

Round 1 (60 minutes — 45 min DSA + 15 min Googlyness)
Problem:

You are given routers with names and their locations in 2D space.
For example:

Router A → (0, 0)
Router B → (0, 8)
Router C → (0, 17)
Router D → (11, 0)
With a wireless range of 10, 
when Router A sends a message, it can reach Router B. Router B can then 
forward it to Router C, but Router D will never receive the message.

Given a list of routers and their coordinates, determine whether
 a message from Router A can reach Router B.

Sample input: [(0,0),(0,8),(0,17),(11,0)], wireless range = 10, source = 0, destination = 3
the source: routers index in the given list, as well as dest
Sample output: False
'''

from collections import deque
from typing import List, Tuple

def can_reach(routers: List[Tuple[int,int]], r: float, source: int, dest: int) -> bool:
    n = len(routers)
    if source == dest:
        return True

    r2 = r * r  # 用平方避免开根号
    q = deque([source])
    visited = [False] * n
    visited[source] = True

    while q:
        u = q.popleft()
        x1, y1 = routers[u]

        for v in range(n):
            if not visited[v]:
                x2, y2 = routers[v]
                dx, dy = x1 - x2, y1 - y2
                if dx*dx + dy*dy <= r2:  # 在范围内就能互相转发
                    if v == dest:
                        return True
                    visited[v] = True
                    q.append(v)

    return False

'''
Time Complexity: O(n²)

原因：
	•	BFS 最多会把每个路由器出队一次（n 次）。
	•	每次出队一个 u，你都用 for v in range(n) 扫一遍所有路由器来找“在范围内的邻居”，这是 O(n)。
	•	所以总计 n * n = O(n²)。

早停（找到 dest 直接 return）只会让平均更快，但 worst-case 仍是 O(n²)。

Space Complexity: O(n)
	•	visited 是 O(n)
	•	队列 q 最多 O(n)
	•	其余常数

'''
# demo
print(can_reach([(0,0),(0,8),(0,17),(11,0)], 10, 0, 3))  # False


import math
from collections import defaultdict, deque

def canReach(routers, startpoint, endpoint, radius):
    # 1) build graph
    adj = {name: [] for name in routers}
    names = list(routers.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            u, v = names[i], names[j]
            x1, y1 = routers[u]
            x2, y2 = routers[v]
            if math.hypot(x1 - x2, y1 - y2) <= radius:
                adj[u].append(v)
                adj[v].append(u)

    # 2) BFS reachability
    if startpoint not in adj or endpoint not in adj:
        return False

    q = deque([startpoint])
    seen = {startpoint}

    while q:
        cur = q.popleft()
        if cur == endpoint:
            return True
        for nei in adj[cur]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return False


'''
Round 2 (45 minutes — DSA Only)

Problem:
Given a binary tree where each node contains only binary values, 
count the number of “islands.”
Follow-up: Count the sizes of each island.

The twist was that the island structure was given as a tree (not a grid). 
I discussed the approach clearly, covered edge cases, and walked through a dry run. 
The interviewer seemed genuinely satisfied with the solution and the thought process.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_islands(root):
    island_count = 0
    
    # helper 判断当前节点是否是一个新岛屿的“入口”
    def dfs(node, parent_val):
        nonlocal island_count
        if not node:
            return
        
        # 如果当前是 1，且父节点是 0（或不存在），说明发现了一个新岛屿
        if node.val == 1 and parent_val == 0:
            island_count += 1
            
        # 继续递归，当前的节点 val 将作为下一层的 parent_val
        dfs(node.left, node.val)
        dfs(node.right, node.val)

    # 初始调用，假设 root 的父节点值为 0
    dfs(root, 0)
    return island_count
# 复杂度分析：
# Time: O(N) 每个节点访问一次
# Space: O(H) H为树高，递归栈空间



#followup quesstion:
class TreeNode:
    def __init__(self,left=None,right=None,val = 0):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_island_on_tree(root:Optional[TreeNode]):

        island_number = 0

        def dfs(node,parent): 
            nonlocal island_number
            if not root:
                return 
            
            if node.val == 1 and parent.val == 0:
                island_number += 1

            dfs(node.left,node.val)
            dfs(node.right,node.val)

        dfs(root,0)
        return island_number
    

    # Follow-up: Count the sizes of each island.
    def count_island_size(root):
        size = []

        def traverse(root):
            if not root:
                return 
            if root.val == 1:
                # 发现岛入口 -> 立刻去吃掉整座岛并数面积，traverse = scan every node, once you see a 1, 
                # that must be a new island (because we will sink islands), so start a DFS to consume it.
                size.append(self.dfs(root))

            traverse(root.left)
            traverse(root.right)

        # dfs 做什么？——“沉岛 + 数面积”
        def dfs(root):
            if not root or root.val == 0:
                return 0
            
            root.val = 0

            return 1 + dfs(root.left) + dfs(root.right)

  # #dfs(node) returns the size of the 1-component connected to this node.
# If node is water (0) or null → size 0.
# Otherwise count itself (1), mark it visited (set to 0), then add sizes from children.     