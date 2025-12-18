class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for a,b in invocations:
            adj[a].append(b)

        S = set()

        def dfs(node:int):
            if node in S:
                return
            S.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(k) #make the covid,collect all the covid in the S

        #then determine if we can remove the collection(S) or not:
        #if we find something comes from the external, then we can not remove it
        #otherwise we can safely remove:

        for a,b in invocations:
            if b in S and a not in S:
                #先遍历所有边，只要发现一条外部->内部就立刻返回全部
                return list(range(n))


        #遍历结束都没发现，再返回删掉 S 的结果
        return list(i for i in range(n) if i not in S)