class Solution:
    #时间复杂度 O(M×N)，其中 M 和 N 是网格的行数和列数
#空间复杂度 O(M×N)，这是由于 DFS 的递归栈在最坏情况下可能会达到 M×N 的深度
    # 主函数，计算岛屿数量
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1

                    self.dfs(grid,i,j)
        return res



    def dfs(self, grid:List[List[str]],i : int, j:int):
        m = len(grid)
        n = len(grid[0])
        #check the boundry make sure don't cause errors
        if i < 0 or j <0 or i >= m or j >= n:
            return

        if grid[i][j] == '0':
            return 

        grid[i][j] = '0'
        self.dfs(grid,  i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i,  j + 1)
        self.dfs(grid, i, j - 1)

