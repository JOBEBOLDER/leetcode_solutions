class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # using max heap and bfs
        #max heap to pop the highest minmum value out:我们想**每次取出路径分数最大的格子（即最大值）**去扩展。

        # 所以说最大堆是维护探索路径的时候的最大值，然后最小值是在这里更新：                    
        # heapq.heappush(heap, (-min(val, grid[ni][nj]), ni, nj))
        m, n = len(grid), len(grid[0])

        visited = set([(0, 0)])
        # 用负数模拟最大堆：优先弹出“当前路径瓶颈值”最大的点
        heap = [(-grid[0][0], 0, 0)]

        # 修正这里：四个方向
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            val, i, j = heapq.heappop(heap)
            val = -val  # 还原成正数（当前到达 (i,j) 的最佳瓶颈值）

            if (i, j) == (m - 1, n - 1):
                return val

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))  # 入堆即标记，表示已以最优瓶颈入堆
                    # 新路径的瓶颈 = min(当前瓶颈, 新格子值)，再取负压入堆（最大堆效果）
                    heapq.heappush(heap, (-min(val, grid[ni][nj]), ni, nj))