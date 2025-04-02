class Solution:
    '''course schedule actually is asking us whether there is a circle happend in graph'''
    '''📈 时间 & 空间复杂度
	•	时间：O(N + E)，其中 N 是课程数，E 是边数（依赖关系数量）
	•	空间：O(N + E)，邻接表、入度表、队列'''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #so we need to construct a graph first:adjacency list
        #想下领结表的形式
        indegree = [0] * numCourses
        adj = defaultdict(list)

        #construct the graph
        for ru,pre in prerequisites:#(ru == 入度,pre == prerequisites)
            indegree[ru] += 1
            adj[pre].append(ru)

        #first implement the in-degree==0 class
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            length = len(q)
            for i in range(length):
                pre = q.popleft()
                numCourses -= 1
                for cur in adj[pre]:
                    indegree[cur] -= 1
                    if indegree[cur] == 0:
                        q.append(cur)

        return numCourses == 0