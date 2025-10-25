class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #一边探索的时候一边弹出最小值，-》最小堆
        # queue：bfs维护探索
    #     这里情况完全相反：
	# •	后来可能会发现一条更平坦的路径（即 effort 更小）到达同一个格子；
	# •	所以一个格子不能“一旦访问过就不再更新”。我们需要记录：当前到达每个格子的“已知最小努力值”。
    # time: O(m n log (m n))
    #space:O(m n)



        m = len(heights)
        n = len(heights[0])
        effort = [[float('inf')] * n for _ in range(m)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        effort[0][0] = 0

        pq = [(0, 0, 0)]   # (当前路径最大差值, x, y)

        while pq:
            cur,i,j = heappop(pq)
            if (i,j) == (m-1,n-1):
                return cur
            for di,dj in directions:
                ni,nj = i + di,j + dj
                if 0 <= ni < m and 0 <=nj < n :
                    # 计算从 (i,j) 走到 (ni,nj) 的 effort
                    new_effort = max(cur, abs(heights[ni][nj] - heights[i][j]))
                    # 如果这条路径更平（更优），则更新
                    if new_effort < effort[ni][nj]:
                        effort[ni][nj] = new_effort
                        heapq.heappush(pq, (new_effort, ni, nj))