class Solution:
    #渔夫可以从任意一个水格开始，
# 然后通过上下左右移动，只能在相连的水格中走动并捞鱼。
# 他能获得的鱼数 = 该连通区域内所有格子的鱼的总和。

	# •	Time: O(m*n) — 每个格子访问一次。
	# •	Space: O(m*n) worst case 递归栈（全图连通）。
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    cur_fish = self.dfs(grid, i, j)
                    ans = max(cur_fish,ans)
        return ans



    def dfs(self, grid,i,j):
        m = len(grid)
        n = len(grid[0])
        fish = 0

        #boundry check:
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0

        #mark as visited
        fish = grid[i][j]
        grid[i][j] = 0
        fish += self.dfs(grid, i+1, j)+self.dfs(grid, i-1, j)+self.dfs(grid, i, j+1)+self.dfs(grid, i, j-1)
        
        return fish
        
        