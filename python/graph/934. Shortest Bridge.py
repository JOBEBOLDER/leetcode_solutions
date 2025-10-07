class Solution:
    #approach: first dfs, find the first island,then all the island to queue, start bfs from this island, 
    #we also need to break once we found the first island, so make suare only one island is processing when doing bfs
#     把两座岛连起来，要求翻转的 0 的最少个数。
# 等价于：从第一座岛 同时 往四周的海水（0）一圈一圈扩散，第一次 碰到另一座岛（1）时，走过的圈数就是最短要翻的 0 的数量。
# 为什么用 found：为了 只 DFS 一次。找到第一块 1 并 DFS 完整座岛后，马上停掉外层扫描，避免把第二座岛也 DFS 进去。
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #first do dfs first
        m = len(grid)
        n = len(grid[0])

        self.found = False
        self.seen = [[False for _ in range(n)] for _ in range(m)]
        self.queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    self.found = True
                    break
            if self.found:
                break
        step = 0
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        #start bfs:
        while self.queue:
            sz = len(self.queue)
            for _ in range(sz):
                x,y = self.queue.popleft()
                for dx,dy in direc:
                    nextx,nexty = dx+x,dy +y
                    if 0 <= nextx < m and 0 <= nexty < n and not self.seen[nextx][nexty]:
                        if grid[nextx][nexty] == 1:
                            # first contact with island B
                            return step
                        # it’s water; expand
                        self.seen[nextx][nexty] = True
                        self.queue.append((nextx, nexty))
            step += 1

        return -1  # should never reach here for valid inputs


    def dfs(self,grid,i,j):
        m = len(grid)
        n = len(grid[0])

        #boundry check:
        if i < 0 or j < 0 or i >= m or j >= n:
            return 

        if grid[i][j] != 1 or self.seen[i][j]:
            return

        self.seen[i][j] = True
        self.queue.append((i,j))
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)



        