class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #special case:
        if not heights or not heights[0]:
            return []

        #initialization
        m = len(heights)
        n = len(heights[0])

        if m == 1 and n == 1:
            return [[0,0]]

        #set to filter the overlap grid
        pacific = set()
        atlantic = set()
        # 从太平洋边界开始DFS (第一行和第一列)
        for i in range(m):
            self.dfs(heights, i, 0, pacific, float('-inf'), m, n)
        for j in range(n):
            self.dfs(heights, 0, j, pacific, float('-inf'), m, n)
        
        # 从大西洋边界开始DFS (最后一行和最后一列)
        for i in range(m):
            self.dfs(heights, i, n-1, atlantic, float('-inf'), m, n)
        for j in range(n):
            self.dfs(heights, m-1, j, atlantic, float('-inf'), m, n)
        
        # 寻找同时能流向太平洋和大西洋的单元格
        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        
        return result

    def dfs(self, heights, i,j,visited, pre_height, m,n):
        #boundry:
        if i<0 or j<0 or i>=m or j>=n or (i,j) in visited or heights[i][j] < pre_height:
            return

        #mark the grid visited:
        visited.add((i,j))

        #move 4 direction:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
        for dx, dy in directions:
            self.dfs(heights, i + dx, j + dy, visited, heights[i][j], m, n)


        '''💡 关键思路（很聪明！）：

        我们不是从每个点出发去试水能不能走到两个海洋，那样效率太低！

        我们反过来想：

            从太平洋边界（上和左）出发，看水能反向“倒着”流回来到哪些格子。

            从大西洋边界（右和下）出发，也看水能反向“倒着”流回来到哪些格子。

        这样我们就得到了两个集合：
            •	pacific_visited：可以被太平洋倒灌到的格子
            •	atlantic_visited：可以被大西洋倒灌到的格子

        最后取交集，就是那些能流到两个海洋的格子！'''