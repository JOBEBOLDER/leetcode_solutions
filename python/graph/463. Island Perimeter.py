class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans= 0
        #for every grid they are island, ans+=4, and two conditions:
            # if this grid the according upper grid it's also a island then -2
            # if this grid the according left grid it's also a island then -2

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4
                    #	•	上方：应当用 i > 0 保护
                    if i > 0 and grid[i-1][j] == 1 : ans -=2 
                    #	左方：应当用 j > 0 保护
                    if  j > 0 and grid[i][j-1] == 1: ans -= 2
        return ans
