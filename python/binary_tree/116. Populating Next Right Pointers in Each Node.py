"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    #medium
    #time:On
    #space: Oh
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1: 'Node', node2: 'Node') -> None:
        if node1 is None and node2 is None:
            return

        # 前序位置 
        # 将传入的两个节点穿起来
        node1.next = node2

        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)

        self.traverse(node1.right, node2.left)