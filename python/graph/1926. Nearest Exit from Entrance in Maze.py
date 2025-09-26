class Solution:
    #plan: the shortest path: bfs
    #start from the entrance point,and bfs all the paths that we can go, output that path number
    ## 标准答案格式：
# Time: O(m*n) - visit each cell at most once
# Space: O(m*n) - visited array or queue in worst case
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        visited = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()

        queue.append((entrance[0],entrance[1]))
        visited[entrance[0]][entrance[1]] = 0

        dires = [(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            sz = len(queue)
            for _ in range(sz):
                x,y = queue.popleft()
                for dx,dy in dires:
                    nextx,nexty = x+dx,y+dy
                    if 0 <= nextx < m and 0 <= nexty < n and maze[nextx][nexty] == '.' and visited[nextx][nexty] == -1:
                        visited[nextx][nexty] = visited[x][y] + 1

                        if nextx == 0 or nextx == m -1 or nexty == 0 or nexty == n - 1:
                            if [nextx, nexty] != entrance:
                                return visited[nextx][nexty]
                        queue.append((nextx,nexty))
                        
        return  -1
