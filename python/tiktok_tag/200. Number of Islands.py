class Solution:
    #islandS
    #GRAPH dfs:
    # time :O(m*n)
    #space:O m*n
    #numIslands：控制总流程 + 找岛起点
#→ 一旦发现岛起点，就调用 dfs 去“标记”（淹）整块岛
#→ 防止之后遍历时重复数同一块岛
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(0, m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)  # 只在找到岛屿时才调用DFS

        return res


    def dfs(self, grid: List[List[str]],i:int, j:int):
        #we need i,j, to keep track of the index of the graph

        # initialization
        m = len(grid)
        n = len(grid[0])

        #edge case ,boundary:

        if i < 0 or j < 0 or i >= m or j >= n:
            return 

        #dfs end condition:
        if grid[i][j] == '0':
            return


        #dfs traverse:
        grid[i][j] = '0'
        self.dfs(grid, i+1,j)
        self.dfs(grid,i - 1, j)
        self.dfs(grid, i, j+ 1)
        self.dfs(grid, i, j- 1)