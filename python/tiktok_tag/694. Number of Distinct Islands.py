class Solution:
    '''time:Om*n
    space:Om*n'''
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 记录所有岛屿的序列化结果
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 淹掉这个岛屿，同时存储岛屿的序列化结果
                    sb = []
                    # 初始的方向可以随便写，不影响正确性
                    self.dfs(grid, i, j, sb, 666)
                    islands.add(tuple(sb))
        # 不相同的岛屿数量
        return len(islands)

    def dfs(self, grid: List[List[int]], i: int, j: int, sb: List[int], dir: int):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return
        # 前序遍历位置：进入 (i, j)
        grid[i][j] = 0
        sb.append(dir)
        
        # 上
        self.dfs(grid, i - 1, j, sb, 1)
        # 下
        self.dfs(grid, i + 1, j, sb, 2)
        # 左
        self.dfs(grid, i, j - 1, sb, 3)
        # 右
        self.dfs(grid, i, j + 1, sb, 4)
        
        # 后序遍历位置：离开 (i, j)
        sb.append(-dir)