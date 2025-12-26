'''
	•	JFK -> [MUC]
	•	MUC -> [LHR]
	•	LHR -> [SFO]
	•	SFO -> [SJC]

    •	你一路往前走，直到走到 死胡同（没有票）。
	•	死胡同最先被写进 res，然后一层层回退，回退时再写。
	•	所以 res 天然是反的，最后必须 reverse。
时间：最坏 O(E^2)
空间：O(E + V)（图存 E 条边 + 递归栈最深 O(E)；结果数组 O(E)）

'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for from_,to in tickets:
            graph[from_].append(to)

        for from_ in graph:
            graph[from_].sort()


        res = []

        def dfs(node:str)->None:
            while graph[node]:
                nxt = graph[node].pop(0)
                dfs(nxt)

            # no outgoing edges left => add to front (like unshift)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]
