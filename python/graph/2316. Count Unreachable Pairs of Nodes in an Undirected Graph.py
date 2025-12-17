class Unionfind():
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        # Path compression
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
            
        return root  # This return was missing

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:  # Only merge if they're not already in the same set
            self.father[root_x] = root_y
            self.num_of_sets -= 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = Unionfind()

        
        for i in range(n):
            uf.add(i)

        for u,v in edges:
            uf.merge(u,v)


        component = defaultdict(int)
        for i in range(n):
            component[uf.find(i)]+=1

        remaining = n
        res = 0
        for s in component.values():
            remaining -= s
            res += s * remaining

        return res
        '''
这里的关键想法

当你处理某个连通块大小 s 时：
	•	还有 remaining 个节点属于“其它还没处理的连通块”
	•	那么这个块里的每个节点，都和那 remaining 个节点不可达
	•	所以新增不可达点对数 = s * remaining
'''