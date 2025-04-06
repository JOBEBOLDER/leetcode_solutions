class Solution:
    '''time:&space=On'''
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
                
                # 记录要反转的数量
        self.res = 0

        # 存储原始边的方向
        roads = set()

        # 构建无向图（邻接表）
        graph = collections.defaultdict(list)

        # 遍历所有连接，记录方向 + 建无向图
        for u, v in connections:
            roads.add((u, v))            # 原始方向 u -> v
            graph[u].append(v)           # 双向
            graph[v].append(u)

        # DFS 主逻辑
        def dfs(u, parent):
            # 如果当前边方向是 parent -> u，说明是错的，需要反转
            if (parent, u) in roads:
                self.res += 1

            # 遍历当前节点 u 的邻居 v
            for v in graph[u]:
                if v == parent:
                    continue              # 防止走回头路
                dfs(v, u)                 # 继续递归访问

        # 从城市 0 开始 DFS
        dfs(0, -1)

        return self.res