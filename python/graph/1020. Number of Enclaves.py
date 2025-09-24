class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        参考：leetcode： 1254 enclosed island
        这道岛屿题目的解法稍微改改就可以解决力扣第 1020 题「飞地的数量」，这题不让你求封闭岛屿的数量，而是求封闭岛屿的面积总和。
        其实思路都是一样的，先把靠边的陆地淹掉，然后去数剩下的陆地数量就行了，非常简单。不过注意第 1020 题中 1 代表陆地，0 代表海水。
	•	Time: O(m * n)	•	Each cell (i, j) is visited at most once:
	•	Space: O(m * n) worst-case recursion stack
'''
        if not grid:
            return 
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
                if grid[i][j] == 1:
                    ans += self.dfs(grid, i, j)

        return ans


    def dfs(self, grid:List[List[int]],i,j):
        if not grid:
            return 
        m = len(grid)
        n = len(grid[0])

        #boundry check:
        if i < 0 or j < 0 or i >= m or j >= n :
            return 0

        #visited check:
        if grid[i][j] == 0:
            return 0
        
        #dfs
        grid[i][j] = 0
        return (1
                + self.dfs(grid, i + 1, j)
                + self.dfs(grid, i - 1, j)
                + self.dfs(grid, i, j + 1)
                + self.dfs(grid, i, j - 1))
