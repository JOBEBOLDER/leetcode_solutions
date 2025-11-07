class Solution:
    #time:Om*n
    #space:
# O(m * n)
# Worst-case recursion depth (single island)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #using dfs to traverse
        m = len(grid)
        n = len(grid[0])
        area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = self.dfs(grid, i, j)
                    area = max(cur_area,area)
        return area
                    


    def dfs(self,grid,i,j):
        #dfs end condiiton:
        m = len(grid)
        n = len(grid[0])

        if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
            return 0

        #dfs 后要mark这个==0
        grid[i][j] = 0
        #递归得search 4 directions area 
        area = 1+ self.dfs(grid, i+1, j)+self.dfs(grid, i-1, j)+self.dfs(grid, i, j+1)+self.dfs(grid, i, j-1)

        return area
