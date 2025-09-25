class Solution:
    
    #use floodfill :
    # 如果grid1的 grid != grid2 grid,it means thery are not sub islands,so floodfill it
    #then iterate the grid2,to see if the grid == 1, then is the sub, that means right now after the floodfill all the remaining grid on the grid2 they are subisland
    #time:m*n
    #space:m*n	•	Space：最坏 O(m*n)（递归栈）
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)#floodfill this grid
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res+= 1
                    self.dfs(grid2, i, j)
        return res



    def dfs(self,grid,i,j):
        m = len(grid)
        n = len(grid[0])

        #boundry check:
        if i <0 or j < 0 or i>=m or j >=n :
            return 


        #visited chck:
        if grid[i][j] == 0:
            return 


        #dfs:
        grid[i][j] = 0
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)