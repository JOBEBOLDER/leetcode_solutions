from collections import Counter
from typing import List, Optional

class TreeNode:
    def __init__(self, val, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.res = []
        self.dfs(root)

        counter = Counter(self.res)
        max_count = max(counter.values())

        ans = []
        for k, v in counter.items():
            if v == max_count:
                ans.append(k)
        return ans

    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.middle)
        self.dfs(root.right)