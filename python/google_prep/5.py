'''
I had previously cleared the screen round of google, so 
I scheduled all the coding rounds on the same day with 1 hour gap. 
Here are the different questions that were asked in each of the rounds:

Round 1
Question: You are given a graph of cities where each vertice denotes a city, 
and the edges represent the connectivity between two cities. 
You can assume that the cost to travel from one city to another connected by a single edge is 1 unit. 

There are two friends Alice and Bob who live in two different cities and want to 
reach to destination city to attend a concert. 
Both Alice and Bob plan to take cabs from their cities to reach the destination. 
They may decide to share a cab in order to minimize the total cost to travel the destination city.
Your task is to find the minimum cost for both Alice and Bob combined to reach destination.
Example:

A - B
|   |
D - C
|   |
E - F
Alice=A, Bob=E, destination=C
Output: 3 (Alice go from A to D, cost=1. Bob go from E to D, cost=1. 
Then both Alice and Bob share a cab from D to C, cost=1. Hence, total cost = 1+1+1 = 3)

My Take: I was not able to solve this problem as I was too fixated on trying to come up with an 
optimal approach so just kept ignoring the interviewer asking me to implement the brute-force solution. 
Would appreciate a lot if someone could provide an optimal solution for this problem, 
and how one shoud approach it!
算法步骤：从 Alice 的起点 A 开始做一次 BFS：得到 A 到所有点的最短距离 distA[]。
从 Bob 的起点 E 开始做一次 BFS：得到 E 到所有点的最短距离 distE[]。
从目的地 C 开始做一次逆向 BFS（无向图直接搜即可）：得到 C 到所有点的最短距离 distC[]。
遍历图中所有的城市 $X$：计算 distA[X] + distE[X] + distC[X]，最小值即为答案。
'''
from collections import deque

def solve():
    # 假设图已经建好为邻接表 adj = {node: [neighbors]}
    # Alice=A, Bob=E, dest=C
    
    def bfs(start_node, n, adj):
        distances = [-1] * (n + 1) # 假设城市编号为 1 to n
        distances[start_node] = 0
        queue = deque([start_node])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    #因为每条边 cost=1，所以从 start 到 neighbor 的最短距离 = 到 curr 的最短距离 + 1。
                    distances[neighbor] = distances[curr] + 1
                    #把这个新发现的城市放进队列，之后继续扩展它的邻居。
                    queue.append(neighbor)
        return distances

    # 1. 三次 BFS
    dist_from_alice = bfs(A, n, adj)
    dist_from_bob = bfs(E, n, adj)
    dist_from_dest = bfs(C, n, adj)
    
    # 2. 遍历所有可能的汇合点 X
    min_total_cost = float('inf')
    
    #把每个城市 i 都当作一个候选“汇合点 X”（Alice 和 Bob 可能在这里碰头）。
    for i in range(1, n + 1):
        # 必须确保三者都能到达该点 X，
        if dist_from_alice[i] != -1 and dist_from_bob[i] != -1 and dist_from_dest[i] != -1:
            current_cost = dist_from_alice[i] + dist_from_bob[i] + dist_from_dest[i]
            min_total_cost = min(min_total_cost, current_cost)
            
    return min_total_cost