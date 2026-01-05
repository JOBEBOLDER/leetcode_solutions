# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List, Tuple

class Solution:
    def goodLeafPairs(self, root: Optional['TreeNode'], distance: int) -> List[Tuple[int, int]]:
        res: List[Tuple[int, int]] = []

        def dfs(node: Optional['TreeNode']) -> List[Tuple['TreeNode', int]]:
            # returns: list of (leafNode, dist from node to leafNode)
            if not node:
                return []

            # leaf
            if not node.left and not node.right:
                return [(node, 0)]

            left_list = dfs(node.left)
            right_list = dfs(node.right)

            # count / collect pairs across left & right
            for leafL, dL in left_list:
                for leafR, dR in right_list:
                    if dL + dR <= distance:
                        res.append((leafL.val, leafR.val))

            # build list to return upward: all leaves' distance + 1, with pruning
            up: List[Tuple['TreeNode', int]] = []
            for leaf, d in left_list + right_list:
                nd = d + 1
                if nd < distance:   # pruning: if nd >= distance, going up only increases it
                    up.append((leaf, nd))

            return up

        dfs(root)
        return res