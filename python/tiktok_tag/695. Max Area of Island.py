class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0  # 记录最大面积
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 计算当前岛屿面积并更新最大值
                    current_area = self.dfs(grid, i, j)
                    max_area = max(max_area, current_area)
        return max_area
    
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # 边界检查
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        if grid[i][j] == 0:
            return 0
        
        # 标记为已访问
        grid[i][j] = 0
        
        # 当前单元格面积为1，加上四个方向的面积
        area = 1 + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + \
                   self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)
        
        return area
        

