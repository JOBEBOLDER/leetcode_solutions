class Solution:
    '''the fact of this quesiton is the same as course schedule,
    the only difference is we need to record the pre course
    
    time:O(E+V)
    space:O(E+V)'''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #initialize of the graph
        indegree = [0] * numCourses
        adj = defaultdict(list)
        result = []

        #construct the graph
        for cur,pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)


        #begin the indegree == 0,# to see which courses do not have any pre, then we can study first

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        #start bfs:
        while q:
            length = len(q)
            for i in range(length):
                pre = q.popleft()
                result.append(pre)

                for cur in adj[pre]:
                    indegree[cur] -= 1
                    if indegree[cur] == 0:
                        q.append(cur)

        return result if len(result) == numCourses else []
        #不equal == 有环


