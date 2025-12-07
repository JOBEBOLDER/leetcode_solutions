class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 1. 初始化变量
        #    - n: grid 大小
        #    - island_id 从 2 开始（因为 grid 当前用 0 和 1）
        #    - 一个字典 area[id] = island 的面积
        m = len(grid)
        n = len(grid[0])
        island_id = 2
        area = {}

        # 2. 第一遍 DFS：遍历整个 grid
        # 目的：把所有岛都编号成 2,3,4,... 且知道每个岛面积
        #    - 遇到 grid[i][j] == 1，则做 DFS，把连通块全部标记成 island_id
        #    - DFS 返回 island 的大小（格子数）
        #    - 把这个面积记录到 area[island_id]
        #    - island_id += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = self.dfs(grid,i,j,island_id)
                    area[island_id] = cur_area
                    island_id += 1


        # 3. 检查特殊情况：如果没有 0，可以直接返回 n * n
        ## 2. 先算一个当前已有岛屿里的最大面积（如果全是 0，这里是 0）
        max_area = 0
        if area:
            max_area = max(area.values())

        # 4. 第二遍遍历 grid
        # 3. 第二遍：枚举每一个 0，看如果把它变成 1，最多能连到多大
        #    - 对每一个 0：
        #         - 查看它四个方向的邻居 (up, down, left, right)
        #         - 收集这些邻居的岛 id（用 set 去重）
        #         - new_area = 1 + sum(area[id] for id in neighbor_islands)
        #         - 更新答案 max_area
        # 5. 返回 max_area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_ids = set()
                    #up
                    if i > 0 and grid[i-1][j] > 1:
                        neighbor_ids.add(grid[i-1][j])
                    #down:
                    if i < m-1 and grid[i+1][j] > 1:
                        neighbor_ids.add(grid[i+1][j])
                    #left:
                    if j > 0 and grid[i][j-1] > 1:
                        neighbor_ids.add(grid[i][j-1])
                    #right:
                    if j < n - 1 and grid[i][j+1] > 1:
                        neighbor_ids.add(grid[i][j+1])
                    new_area=1
                    for ids in neighbor_ids:
                        new_area += area[ids]
                    max_area = max(max_area,new_area)
         # 4. 如果没有 0，被上面第二遍完全没更新，那 max_area 就是原始岛屿最大面积
        #    对于全是 1 的情况，max_area 会是 n*n
        #    对于全是 0 的情况，max_area 会是 0（但题目允许改一个 0 -> 1，所以答案至少 1）
        if max_area == 0:  # 特殊情况：全 0 的 grid
            return 1

        return max_area

    def dfs(self, grid, i, j, island_id):
        m = len(grid)
        n = len(grid[0])
        # DFS 作用：
        #   - 将连通的 1 都涂成 island_id
        #   - 返回该岛的面积

        # 1. 越界 or 遇到 0 → return 0
        if i >= m or i < 0 or j >= n or j < 0:
            return 0
        if grid[i][j] != 1:
            return 0

        # 2. 把当前格子标记为 island_id
        grid[i][j] = island_id

        # 3. 从四个方向累加面积
        #    area = 1
        #    area += dfs(上下左右)
        area = 1
        #累加四个方向的面积
        area += self.dfs(grid,i+1,j,island_id)
        area += self.dfs(grid,i-1,j,island_id)
        area += self.dfs(grid,i,j+1,island_id)
        area += self.dfs(grid,i,j-1,island_id)

        # 4. return area
        return area