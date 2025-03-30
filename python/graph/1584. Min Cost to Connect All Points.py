class UnionFind:
    #medium 
    #space:On
    #time:O^2
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0

    def add(self, x):
        # initialization
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1

    def find(self, x):
        root = x
        #先找爹
        while self.father[root] != None:
            root = self.father[root]

        # compress the root:#再带领其他人认领爹
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root 

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        # 创建边列表，计算所有点对之间的曼哈顿距离
        #time:O^2
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                # 计算曼哈顿距离: |xi - xj| + |yi - yj|
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, dist))
        
        # 按距离排序
        edges.sort(key=lambda x: x[2])
        
        # 初始化并查集
        uf = UnionFind()
        for i in range(n):
            uf.add(i)
        
        # Kruskal算法
        total_cost = 0
        edge_count = 0
        
        for u, v, cost in edges:
            # 如果两点不在同一个集合中，则连接它们
            if uf.find(u) != uf.find(v):
                uf.merge(u, v)
                total_cost += cost
                edge_count += 1
                
                # 提前结束：MST需要n-1条边
                if edge_count == n - 1:
                    break
        
        return total_cost