'''
There are N coins valued (0 to N - 1).
Calculate no. of ways to select K coins such that their sum is divisible by M.
Return answer modulo 1e9 + 7.
int solve(int N, int M, int K)
Input:
4 2 2
Output: 2

Constraints:
1 <= N, M, K <= 10^3

Given tree graph with N nodes/regions (1 to N) and (N - 1) bidirectional edges/roads.
Each node/region (i + 1) has no. of towns denoted by towns[i].
Calculate min difference in total sum of towns between resulting components 
when you delete one edge.
int minTownsDiff(int N, vector<int>& towns, vector<vector<int>>& roads)
Input:
2
10 20
1 2
Output: 10

Constraints:
1 <= N <= 10^5
1 <= towns[i] <= 10^4


'''

import sys
from math import inf

# 递归深度上限：N 最多 1e5，树可能退化成链，递归深度也可能到 1e5
sys.setrecursionlimit(200000)

def minTownsDiff(N, towns, roads):
    # 建邻接表：adj[u] 存 u 的所有相邻节点
    # 用 N+1 是因为节点编号是 1..N
    adj = [[] for _ in range(N + 1)]

    # roads 里每条边 (u, v) 是双向的
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    # 树上所有节点的城镇总和
    # towns 是 0-indexed：towns[i] 表示节点 i+1 的城镇数
    total_sum = sum(towns)

    # 可选：保存每个节点的子树和（你代码里创建了，但其实不一定要用）
    self_subtree_sums = [0] * (N + 1)

    # 初始化最小差值为无穷大
    min_diff = inf

    def dfs(u, p):
        """
        返回：以 u 为根的子树城镇总和
        p：u 的父节点，防止走回头路
        """
        nonlocal min_diff  # 允许修改外层变量 min_diff

        # curr_sum 初始等于当前节点自己的城镇数
        # u 是 1..N，所以对应 towns[u-1]
        curr_sum = towns[u - 1]

        # 遍历 u 的邻居
        for v in adj[u]:
            # v != p：跳过父节点，避免在无向图里来回走
            if v != p:
                # 先算子树和（后序思想）
                child_sum = dfs(v, u)
                # 把子树和加到当前子树和里
                curr_sum += child_sum

        # curr_sum 此时就是 u 子树的总城镇数
        self_subtree_sums[u] = curr_sum

        # 只要 u 不是根节点，就可以“切断 u 和父节点 p 的那条边”
        # 切断后，一边是 u 子树（curr_sum），另一边是 total_sum - curr_sum
        if p != -1:
            # 组件差值 = |(total_sum - curr_sum) - curr_sum|
            #          = |total_sum - 2*curr_sum|
            diff = abs(total_sum - 2 * curr_sum)
            # 更新答案
            if diff < min_diff:
                min_diff = diff

        # 把当前子树和返回给父节点
        return curr_sum

    # 随便选 1 做根，从 1 开始 DFS
    dfs(1, -1)

    return min_diff