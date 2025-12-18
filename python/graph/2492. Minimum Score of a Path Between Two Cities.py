class Solution:
    '''
    list of of the possible path from 1-n,
    and also and the same time maintance one variable min_val to update as the result
    -because it's a graph, need visited in case cycles

    use dfs:
    traversal from 1-n ,explore all the possibale way to get to n

    “Time is O(V+E). Space is O(V+E) for the adjacency list plus O(V) for visited, and recursion stack is O(V) in the worst case.”

    
    '''
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #build the graph first
        #then dfs the connected componnent to find and update the glbal variable min_score
        adj = defaultdict(list)
        for a,b,dis in roads:
            adj[a].append([b,dis])
            adj[b].append([a,dis])

            visited = set()

            min_score = float('inf')

        def dfs(u:int):
            nonlocal min_score
            visited.add(u)
            for nei,dis in adj[u]:
                min_score = min(min_score,dis)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return min_score

'''
adj[1] = {4: w7, 2: w9}
adj[2] = {1:w9,4:w5,3:w6}
adj[3] = {2:w6}
adj[4] = {1:w7,2:w5}


visited = set(1, 4,2,3)
min_score = 5

'''

