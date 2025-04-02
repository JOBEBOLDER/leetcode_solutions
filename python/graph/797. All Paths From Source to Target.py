class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.dfs(graph, 0)
        return self.res



    def dfs(self, graph:List[List[int]],s:int):
        #enter the graph
        self.path.append(s)

        #endcondition
        n = len(graph)
        if s == n - 1:
            self.res.append(self.path.copy())
            self.path.pop()
            return


        for v in graph[s]:
            self.dfs(graph, v)

        self.path.pop()


