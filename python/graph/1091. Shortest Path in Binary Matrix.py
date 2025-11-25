class Solution:
    '''
    BFS 如果不存在“回头路”，就不需要 visited。**
	•	tree → ✔ 不会回头 → 不需要
	•	graph/grid → ❌ 会回头 → 必须
        visited: O(N²)
        queue:  O(N²)
        总空间：O(N²)
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        #base case
        if not grid or grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        #bfs initializaiton:
        queue = deque()
        path = 1 #maintenance the result,cell itself it's 1
        queue.append((0,0))
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        direc = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

        while queue:
            sz = len(queue)
            for i in range(sz):
                x,y = queue.popleft()

                #check end condition:
                if x == m-1 and y == n - 1:
                    return path
                for dx,dy in direc:
                    nextx,nexty = dx+x,dy+y
                    if 0 <= nextx < m and 0 <= nexty < n and grid[nextx][nexty] == 0 and not visited[nextx][nexty]:
                        queue.append((nextx,nexty))
                        visited[nextx][nexty] = True
            path += 1

        return -1





        
                