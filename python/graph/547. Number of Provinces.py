class UnionFind:
    #time:On^2
    #space:On
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0

    #👶 add(x)：加入一个新城市（最开始是独立的）
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1

    #find(x)：找到某个城市的“祖宗”
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root] #一直向上找爸爸
        #路径压缩
        while x!= root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    #merge(x, y)：把两个城市合并为一个集合
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y    # 把x集合挂到y集合下
            self.num_of_sets -= 1           # 两个合并了，集合数减1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):# 每个城市加入集合
            uf.add(i)
            for j in range(i):
                if isConnected[i][j] == 1:
                    uf.merge(i,j)# 合并他们的朋友圈

        return uf.num_of_sets      # 返回朋友圈的数量
        