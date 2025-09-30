class Solution:
    #approach: start from all the land, using queue,
    #bfs search for all the water, recording the steps we need to make from each island,
    #pick the most steps one
    #time:Om*n
    #space:Om*n
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        visited = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited[i][j] = 0

        dirc = [(1,0),(-1,0),(0,-1),(0,1)]

        res = -1
        while queue:
            sz = len(queue)
            for _ in range(sz):
                x,y = queue.popleft()
                for dx,dy in dirc:
                    nextx,nexty = dx+x,dy+y
                    if 0 <= nextx < m and 0 <= nexty < n and visited[nextx][nexty] == -1 and grid[nextx][nexty] == 0:
                        visited[nextx][nexty] = visited[x][y] + 1
                        res = max(res,visited[nextx][nexty])
                        queue.append((nextx,nexty))


        return res
                    
        

