class UnionFind():
    def __init__(self):
        self.father = {}
        self.nums_of_sets = 0

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.nums_of_sets += 1

    def find(self, x):
        # find the dad
        root = x
        while self.father[root] != None:
            root = self.father[root]

        # compress the path:
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root  # You were missing this return statement

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y  # Should be root_x, not x
            self.nums_of_sets -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize UnionFind
        uf = UnionFind()
        
        # Add all nodes
        for i in range(n):
            uf.add(i)
        
        # Process all edges
        for edge in edges:
            u, v = edge[0], edge[1]
            uf.merge(u, v)
        
        return uf.nums_of_sets