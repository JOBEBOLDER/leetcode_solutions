class Solution:
#     🔹 “反向建图”：
# 原图中 u → v 表示 “u 是 v 的祖先”。
# 为了从子节点往上找祖先，我们反向保存成 v → u。
# 这样在 DFS 时，从 v 出发可以访问所有它的祖先节点。

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)  # 反向建图

        ans = []
        for i in range(n):
            #防止循环
            visited = set()
            self.dfs(i, graph, visited)
            ans.append(sorted(list(visited)))
        return ans

    def dfs(self, node, graph, visited):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                self.dfs(nei, graph, visited)