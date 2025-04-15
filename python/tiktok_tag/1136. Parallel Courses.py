class Solution:
    #time: OV+E
    #space:OV+E
    #是因为每个节点和每条边都只是访问一次
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #initialization variable for building graph
        adj = defaultdict(list)
        indegree = [0] * n


        #building the graph
        for pre, cur in relations:
            adj[pre - 1].append(cur - 1)
            indegree[cur - 1] += 1

        q = deque()
        #find the indegree ==0 ,means we can traverse first:
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)


        learned = 0
        res = 0
        while q:
            res += 1 #每一轮，每一层是一个学期
            length = len(q)
            for i in range(length):
                pre = q.popleft()
                learned += 1
                for cur in adj[pre]:
                    indegree[cur] -= 1
                    if indegree[cur] == 0:
                        q.append(cur)
        return res if learned == n else -1



        
