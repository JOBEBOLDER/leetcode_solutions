class Solution:
    '''
    first: use dfs to find the first island
    second: use bfs to find the second one, when find one, we increase the layer by one'''
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.visited = [[False] * n for _ in range(m)]
        self.queue = deque()
        found = False

        # Step 1: DFS 找到第一个岛屿并把它所有的点加入 queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    found = True
                    break
            if found:
                break

        # Step 2: BFS 从第一个岛屿出发，寻找最短的“桥”
        steps = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while self.queue:
            for _ in range(len(self.queue)):
                x, y = self.queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not self.visited[nx][ny]:
                        if grid[nx][ny] == 1:
                            return steps  # 成功连接到第二个岛
                        self.queue.append((nx, ny))
                        self.visited[nx][ny] = True
            steps += 1

        return -1  # 不应该走到这里


    def dfs(self,grid:List[List[int]],i:int, j:int):
        m = len(grid)
        n = len(grid[0])

        #base case boundry:
        if i < m or j < n or i >= m or j >= n:
            return 

        if grid[i][j]!= 1 or grid[i][j]:
            return
        grid[i][j] = True
        self.queue.append((i, j))  # 加入到 BFS 起点队列

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)