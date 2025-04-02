class Solution:
    '''🧠 关键观察（人话版）
	有入边的点，说明“别人可以走到我”；
没有入边的点，说明“我必须是某人的出发点”。
所以：=✅ 所有没有入边的点，一定是你需要的“起点”。'''

#time:O(E+n)	•	遍历所有边：O(E)（E 是边数）•	把终点放入 set（插入 set 平均是 O(1)）：总共 O(E)
#space:On
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        endSet = set(y for x,y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans