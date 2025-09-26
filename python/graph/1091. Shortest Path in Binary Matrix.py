class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #base case:
        if not grid or grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1


        #bfs:queue
        queue = deque()
        visited = [[False] * n for _ in range(m)]
        queue.append((0,0))
        visited[0][0] = True

        path = 1

        dirc = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        while queue:
            sz = len(queue)
            for _ in range(sz):
                x,y = queue.popleft()
                #check end condition:
                if x == m - 1 and y == n - 1:
                    return path

                for dx,dy in dirc:
                    nextx,nexty  = dx + x, dy + y
                    if 0 <= nextx < m and 0 <= nexty < n and grid[nextx][nexty] == 0 and not visited[nextx][nexty]:
                        queue.append((nextx,nexty))
                        visited[nextx][nexty] = True
            path += 1
        return -1

                