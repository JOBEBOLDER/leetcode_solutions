from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None
    nodes = [None if v is None else TreeNode(v) for v in arr]
    for i in range(len(arr)):
        if nodes[i] is None:
            continue
        l, r = 2 * i + 1, 2 * i + 2
        if l < len(arr):
            nodes[i].left = nodes[l]
        if r < len(arr):
            nodes[i].right = nodes[r]
    return nodes[0]

def serialize(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    q = deque([root])
    out = []
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    # remove the None at the end and keep the None in the middle
    while out and out[-1] is None:
        out.pop()
    return out

def delete_tree(arr: List[Optional[int]], to_delete: List[int]) -> List[List[Optional[int]]]:
    root = build_tree(arr)
    if not root:
        return []

    delete_set = set(to_delete)
    forest_roots = []

#“dfs returns the root of the remaining subtree so the parent can reconnect pointers.
# We only push nodes into forest_roots when they become new roots—i.e., their parent is deleted (or the original root survives).”
    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        node.left = dfs(node.left)
        node.right = dfs(node.right)

        if node.val in delete_set:
            if node.left:
                forest_roots.append(node.left)
            if node.right:
                forest_roots.append(node.right)
            return None
        #The task of dfs(node) is not to ‘collect answers’, but to ‘trim the tree and return the trimmed root’.
        return node

    new_root = dfs(root)
    if new_root:
        forest_roots.append(new_root)

    return [serialize(r) for r in forest_roots]