class Solution:
        # '''：凡是接触到边界的“陆地岛”（0 连通块）都不算封闭岛。
        # 做法就是：先把所有“贴着边界的 0 岛”淹掉/标记掉，剩下还没被淹到的 0 连通块就是“封闭岛”（四面都被 1 包围、且不触边）。
        # '''
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            self.dfs(grid, i, 0) #left boundry
            self.dfs(grid,i,n-1) #right boundry

        for j in range(n):
            self.dfs(grid,0,j) #upper boundry
            self.dfs(grid,m-1,j) #lower boundry

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
                    self.dfs(grid, i, j)

        return ans


    def dfs(self, grid:List[List[int]],i,j):
        m = len(grid)
        n = len(grid[0])

        #boundry check:
        if i < 0 or j < 0 or i >= m or j >= n :
            return 

        #visited check:
        if grid[i][j] == 1:
            return 
        
        #dfs
        grid[i][j] = 1
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
