class Solution:
    #time:m*n,Each cell enqueued once, each direction explored efficiently
    #易错点：开始时候把起点加入visited
    #while 0 <= nextx < m and 0 <= nexty < n and maze[nextx][nexty] == 0:这个边界条件
    #出界之后要回来
    #queue加入的是一个turple（（x,y））

    #space:O(m·n)visited + queue

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        #initialization
        m = len(maze)
        n = len(maze[0])

        # queue,visited, direc:
        queue = deque()
        visited = [[False] * n for _ in range((m))]
        direc = [(1,0),(0,1),(-1,0),(0,-1)]

        queue.append((start[0],start[1]))
        visited[start[0]][start[1]] = True

        while queue:
            sz = len(queue)
            for _ in range(sz):
                x,y = queue.popleft()
                for dx,dy in direc:
                    nextx,nexty = x,y
                    #只要我还没出门（没出界）并且没撞到墙，我就继续走。”
                    while 0 <= nextx < m and 0 <= nexty < n and maze[nextx][nexty] == 0:
                        nextx += dx
                        nexty += dy

                    #刚才多走了一步（撞墙/出界），退回到上一个合法点。”
                    nextx -= dx
                    nexty -= dy

                    if [nextx,nexty] == destination:
                        return True

                    if not visited[nextx][nexty]:
                        visited[nextx][nexty] = True
                        queue.append(([nextx, nexty]))

        return False


