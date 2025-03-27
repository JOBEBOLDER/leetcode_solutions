"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 施展链表双指针技巧
        a, b = p, q
        while a != b:
            # a 走一步，如果走到根节点，转到 q 节点
            a = q if a is None else a.parent
            # b 走一步，如果走到根节点，转到 p 节点
            b = p if b is None else b.parent
        return a