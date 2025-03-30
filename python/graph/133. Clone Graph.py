"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''我们要“复制图”——其实就是把每个节点“重新生成一个一模一样的新节点”，并连接它的新邻居。
图的问题通常要用 DFS 或 BFS 遍历整张图，然后“边遍历边复制”。
⚠️ 重点是防止死循环！'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.lookup = {}
        return self.dfs(node)

    def dfs(self, node:Optional['Node']):
        #if we already had the node
        if node in self.lookup:
            return self.lookup[node]

        #if not,we create a new one and add the loopup
        clone = Node(node.val,[])
        self.lookup[node] = clone

        #clone the neighbour
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor))

        return clone