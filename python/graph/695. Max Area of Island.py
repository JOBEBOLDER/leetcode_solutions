class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #after dfs assign value to one variable then update the result
                    cur_area = self.dfs(grid,i,j)
                    res = max(cur_area,res)
        return res


        
    def dfs(self,grid:List[List[int]],i,j):
            m = len(grid)
            n = len(grid[0])

            #boundry check:
            if i < 0 or  j < 0 or i >= m or j >= n :
                return 0

            #细节错了，记得mark是算0，不是#，因为这题算的是面积
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1+ self.dfs(grid,i+1,j)+self.dfs(grid,i - 1,j)+self.dfs(grid,i,j+1)+self.dfs(grid,i,j-1)
            return area
