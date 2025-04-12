class Solution:
    '''time:  O(n * m)
    space: O(n * m)'''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first i need to calculate all the fresh oranges 
        m = len(grid)
        n = len(grid[0])
        fresh =  0
        q = []

        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i,j))


        ans = 0
        while q and fresh:
            ans += 1 # already passed 1 min
            tmp = q # use tmp to traverse
            q = [] #empty the q and for next round queue

            for x, y in tmp:
                for i, j in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # 新鲜橘子
                        fresh -= 1
                        grid[i][j] = 2 #mark as rotten oranges
                        q.append((i,j))
        return -1 if fresh else ans



        




