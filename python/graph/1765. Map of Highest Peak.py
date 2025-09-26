class Solution:
    #plan:If the cell is a water cell, its height must be 0.
    #so bfs,mark all the water to 0,then bfs all the adjecant grids by adding one each layer
    #time:m*n
    #space:M*n
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        visited = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    visited[i][j] = 0
                    queue.append((i,j))
        
        #start bfs:
        dires = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            x,y = queue.popleft()
            for dx,dy in dires:
                nextx,nexty = dx+x,dy+y
                if 0 <= nextx < m and 0 <= nexty < n and visited[nextx][nexty] == -1:
                    queue.append((nextx,nexty))
                    visited[nextx][nexty] = visited[x][y] + 1
        return visited