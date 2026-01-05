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

Round 2 (45 minutes — DSA Only)
This round went significantly better. My interviewer was someone I recognized from Instagram/LinkedIn (a known tech influencer), and the interaction was smooth and positive.

Problem:
Given a binary tree where each node contains only binary values, count the number of “islands.”
Follow-up: Count the sizes of each island.

The twist was that the island structure was given as a tree (not a grid). I discussed the approach clearly, covered edge cases, and walked through a dry run. The interviewer seemed genuinely satisfied with the solution and the thought process.
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