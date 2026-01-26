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

My interviewer joined around 25 minutes late. Coincidentally, 
I had another (on-campus) interview that day with only a 20-minute gap between the two, 
so the delay added a lot of stress.

The problem itself was straightforward, and I was able to solve and code it. However, 
the overall interaction was uncomfortable.
 While I was coding and explaining my thought process (as generally encouraged), 
 the interviewer abruptly told me to stop speaking and just write the code. 
 After I completed my solution, she spent around 5–7 minutes checking it line-by-line 
 against what seemed like an internal reference solution. 
 The tone throughout the conversation felt irritated and dismissive, 
 which made the experience quite difficult despite my maintaining professionalism.


'''
'''
import math

def can_reach(routers, start_node, end_node, radius):
    # routers: { "A": (0,0), "B": (0,8), ... }
    
    # 1. 建图 (Adjacency List)
    adj = {name: [] for name in routers}
    names = list(routers.keys())
    
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            u, v = names[i], names[j]
            x1, y1 = routers[u]
            x2, y2 = routers[v]
            # 计算欧几里得距离
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if dist <= radius:
                adj[u].append(v)
                adj[v].append(u)
    
    # 2. BFS 寻找路径
    if start_node not in adj or end_node not in adj:
        return False
        
    queue = [start_node]
    visited = {start_node}
    
    while queue:
        curr = queue.pop(0)
        if curr == end_node:
            return True
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

'''

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
This round went significantly better. My interviewer was someone I recognized from Instagram/LinkedIn (a known tech influencer), and the interaction was smooth and positive.

Problem:
Given a binary tree where each node contains only binary values, count the number of “islands.”
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

def count_tree_islands(root):
    island_sizes = []
    
    # helper 负责遍历并“消灭”整个岛屿，返回岛屿大小
    def dfs(node):
        if not node or node.val == 0:
            return 0

        node.val = 0  # 标记已访问/沉岛

        left_size = dfs(node.left)     # 左子树这部分岛屿的面积
        right_size = dfs(node.right)   # 右子树这部分岛屿的面积

        size = 1 + left_size + right_size  # 自己(1) + 左 + 右
        return size
    
    # 主函数：寻找每一个岛屿的起点
    def traverse(node):
        if not node:
            return
        
        if node.val == 1:
            # 发现新岛屿，开始 DFS 统计大小
            island_sizes.append(dfs(node))
            
        # 注意：即便当前是 0 或 1，都要继续看子节点
        # 因为 0 的下面可能还有新的 1（新的岛屿）
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return len(island_sizes), island_sizes

# 复杂度分析：
# Time: O(N) 每个节点访问一次
# Space: O(H) H为树高，递归栈空间