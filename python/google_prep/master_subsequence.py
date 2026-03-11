'''
题目描述 (Original Problem Reconstruction)
Title: Consistent Master Sequence Reconstruction

Problem Statement: 我们有一个包含多个子序列（subsequences）的列表
 List<List<Integer>> subsequences。已知这些子序列都是从同一个 Master Sequence 中通过删除零个或多个元素得到的。

这个 Master Sequence 有两个关键属性：

它包含一组唯一的整数（没有重复数字）。

它定义了这些数字之间的绝对顺序。

Your Task: 编写一个函数，判断给定的这些子序列是否“一致（Consistent）”。也就是说，是否存在至少一个 Master Sequence，能够同时满足所有子序列中定义的相对顺序。

Example 1:

Input: [[1, 2, 5], [2, 3, 4]]

Output: True

Explanation: 存在一个 Master Sequence 如 [1, 2, 3, 4, 5] 可以生成这两个子序列。

Example 2:

Input: [[1, 2, 5], [2, 1]]

Output: False

Explanation: 第一个序列要求 1 在 2 之前，而第二个要求 2 在 1 之前。这产生了矛盾，无法形成统一的 Master Sequence。


用人话翻译题目

每个 subsequence 都在告诉你一些规则，比如：
	•	[1, 2, 5] 的意思不是“必须挨着”，而是：
	•	1 在 2 前面
	•	2 在 5 前面
	•	所以也暗含 1 在 5 前面

把所有 subsequence 的这些“必须先后”的规则收集起来，你要判断：

能不能给所有数字排一个队，让所有“谁在谁前面”的规则都满足？

⸻

什么时候会 False？

只要出现矛盾的先后关系，就会 False。最典型是形成“循环”：
	•	一个序列说 1 在 2 前（1 -> 2）
	•	另一个说 2 在 1 前（2 -> 1）

这就变成：1 要在 2 前，同时 2 又要在 1 前，不可能。

更一般的循环也不行，比如：
	•	1 -> 2, 2 -> 3, 3 -> 1
这叫“环”，也不可能排队。

⸻

这题为什么用图/拓扑排序？

因为这题等价于：
	•	把每个“必须在前面”的关系当作一条有向边 u -> v
	•	问：这个有向图里有没有环？
	•	没环：就能拓扑排序 → 存在 Master Sequence → True
	•	有环：无法拓扑排序 → 不存在 Master Sequence → False

'''

from collections import defaultdict, deque
from typing import List
# subsequences = [[1, 2, 5], [2, 1]]
# subsequences = [[1, 2, 5], [2, 4], [4, 5]]
def can_form_master_sequence(subsequences: List[List[int]]) -> bool:
    # 1. 构建图和入度表
    # adj: 邻接表，存储谁在谁后面 (1 -> 2)
    # in_degree: 统计每个数字有多少个“前置依赖”
    adj = defaultdict(set)
    in_degree = defaultdict(int)
    nodes = set()
    
    for sub in subsequences:
        for i in range(len(sub)):
            nodes.add(sub[i])
            # 建立相邻两个元素的顺序关系
            if i > 0:
                u, v = sub[i-1], sub[i]
                if v not in adj[u]:
                    adj[u].add(v)
                    in_degree[v] += 1
    
    # 2. 找到所有入度为 0 的节点（即没有前置依赖的数字）
    queue = deque([node for node in nodes if in_degree[node] == 0])
    
    # 3. 拓扑排序：不断取出入度为 0 的点并移除
    visited_count = 0
    while queue:
        curr = queue.popleft()
        visited_count += 1
        
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
# 4. 如果最后处理过的节点数等于总节点数，说明没有环，返回 True
    return visited_count == len(nodes)

# --- 测试用例 ---
# print(can_form_master_sequence([[1, 2, 5], [2, 3, 4]])) # True
# print(can_form_master_sequence([[1, 2, 5], [2, 1]]))    # False
'''
	•	扫描所有 subsequences 的元素：O(total_elements)
	•	每次相邻对用 set 去重，平均 O(1)
所以整体可写成：O(total_elements + E)（通常简写为 O(total_elements)）

	2.	拓扑排序（Kahn BFS）

	•	每个点入队出队一次：O(V)
	•	每条边被“减入度”一次：O(E)

✅ 总时间：O(total_elements + V + E)
常见简写：O(V + E)（因为建图也就是把这些边读进来）

⸻

Space
	•	adj 存边：O(E)
	•	in_degree 存每个点：O(V)
	•	nodes：O(V)
	•	queue 最多装 V 个：O(V)

✅ 总空间：O(V + E)


'''