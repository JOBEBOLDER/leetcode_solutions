from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        queue = deque()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        # dist[x][y]：从 start 滚到并停在 (x,y) 的最短距离；-1 表示未到达
        dist = [[-1 for _ in range(n)] for _ in range(m)]

        sx, sy = start
        gx, gy = destination

        queue.append((sx, sy))
        dist[sx][sy] = 0

        while queue:
            x0, y0 = queue.popleft()          # 固定当前“停点”作为四个方向的共同起点
            base = dist[x0][y0]

            for dx, dy in dirs:
                x, y = x0, y0                  # 每个方向都从 (x0,y0) 开始滚
                steps = 0

                # 一直滚到撞墙前一格
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    steps += 1

                if steps == 0:                 # 这个方向没动，不用入队
                    continue

                nd = base + steps              # 新的更短距离？
                #如果我们通过当前路径，发现从起点滚到 (x,y) 的距离 更短了，
                #那么就更新这点的最短距离，并让它 重新入队，从这里继续扩展。
                if dist[x][y] == -1 or nd < dist[x][y]:
                    dist[x][y] = nd
                    queue.append((x, y))

        return dist[gx][gy]