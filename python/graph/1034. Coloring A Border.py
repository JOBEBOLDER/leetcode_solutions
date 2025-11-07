class Solution:
    '''
    understand:
    input:m*n grid, 3 ints: 
    rules:
    	•	返回 1 → 表示当前方向“触到了边界”：
	•	越界（i<0/j<0/i>=m/j>=n）；
	•	或者相邻格颜色不同。
	•	返回 0 → 表示当前方向是安全的、在连通块内部。
    
    '''
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        tcolor = grid[row][col]
        visit = [[False]*n for _ in range(m)]
        def dfs(i,j):
            if  i < 0 or j < 0 or i >= m or j >= n:
                return 1
            if visit[i][j]:
                return 0
            if grid[i][j] != tcolor:
                return 1
            visit[i][j] = True
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if  dfs(x,y)==1:
                    grid[i][j] = color
            return 
        dfs(row,col)
        return grid



