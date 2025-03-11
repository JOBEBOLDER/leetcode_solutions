"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        lookup = {} #hashmap

        #base case
        if not node:
            return None

        def dfs(node):
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])

            lookup[node] = clone

            for  n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)