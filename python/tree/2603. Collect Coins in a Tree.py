from collections import deque, defaultdict
from typing import List
#time and space:On

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if n <= 1:
            return 0

        graph = defaultdict(list)
        indegree = [0] * n   # 这里的 indegree 实际上就是“度数 degree”

        # 1) build undirected graph + degree
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        # ------------------------------------------------------------
        # Topo 1: 连锁修剪 —— 删掉所有 "叶子且没有 coin" 的节点
        # queue 里放：indegree==1 且 coins==0 的点
        # 删掉一个点会让它的邻居度数 -1，邻居可能也变成叶子且没 coin -> 继续删
        # ------------------------------------------------------------
        queue = deque()
        for i in range(n):
            if indegree[i] == 1 and coins[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()

            # 如果已经被删过，跳过
            if indegree[cur] == 0:
                continue

            # 删除 cur（标记为 0 表示不在树里了）
            indegree[cur] = 0

            # cur 在树里是叶子，影响它的邻居
            for nei in graph[cur]:
                if indegree[nei] == 0:   # 邻居也可能已经被删了
                    continue

                indegree[nei] -= 1

                # 关键：Topo1 只删 "没 coin 的叶子"
                if indegree[nei] == 1 and coins[nei] == 0:
                    queue.append(nei)

        # ------------------------------------------------------------
        # Topo 2: 在剩余树上，再删“两层叶子”
        # 理由：coin 可在距离 <= 2 内收集，所以最外层两圈边都不必走进去
        # 做法：把当前所有叶子入队，然后按层删除两轮（必须按层）
        # ------------------------------------------------------------
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)

        for _ in range(2):  # 删除两层（只删 2 “层”叶子，不是删到空）
            length = len(queue)  # 这一轮开始时，队列里“当前这一层的叶子”有多少个；固定住，确保只删这一层
            for _ in range(length):
                cur = queue.popleft()
                if indegree[cur] == 0:  # 如果 cur 之前已经被删掉（可能重复入队），就跳过
                    continue

                # 删除 cur：把它从“剩余树”里移除
                indegree[cur] = 0  # 标记 cur 不再存在于图里（度数设为 0）

                for nei in graph[cur]:  # 遍历 cur 的邻居：cur 被删会影响邻居的度数
                    if indegree[nei] == 0:  # 如果邻居本身也已经被删了，就不用处理
                        continue

                    indegree[nei] -= 1  # cur 被删，相当于 nei 少了一条连接边，所以度数 -1

                    if indegree[nei] == 1:  # 如果 nei 现在变成“叶子”了
                        queue.append(nei)   # 把它加入队列：它会在“下一轮/下一层”被删（注意：不是马上删）

        # ------------------------------------------------------------
        # 统计剩余节点数 remain（还在核心子树里的点）
        # 树里 remain 个点 => remain-1 条边
        # 为了覆盖核心子树，边需要往返走：2*(remain-1)
        # remain <= 1 时没有边可走，答案为 0
        # ------------------------------------------------------------
        remain = sum(1 for d in indegree if d > 0)#？？？ 
        return 0 if remain <= 1 else (remain - 1) * 2 #求有效的点的edge = (remain - 1) * 2