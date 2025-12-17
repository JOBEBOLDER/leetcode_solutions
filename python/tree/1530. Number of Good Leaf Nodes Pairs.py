# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.distance = distance
        self.ans = 0
        self.dfs(root)
        return self.ans


    def merge(self,left:List[int],right:List[int])->None:
        for l in left :
            for r in right:
                if l+r <= self.distance:
                    self.ans += 1


    def dfs(self,root)->List[int]:
        # base case:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [1]

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        #postorder:
        self.merge(left,right)
        
        #optimzation:
        res = []
        for d in left+right:
            nd = d + 1
            if nd < self.distance:
                res.append(nd)
        return res

#如果输出格式改成turple的pair:List:[Tuple[int,int]]
from typing import Optional, List, Tuple

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findGoodPairs(self, root: Optional['TreeNode'], distance: int) -> List[Tuple[int, int]]:
        self.dist = distance
        self.res: List[Tuple[int, int]] = []
        self.dfs(root)
        return self.res

    def merge_collect(self, left: List[Tuple[int, int]], right: List[Tuple[int, int]]) -> None:
        # left/right: [(leafVal, distToCurrentNode), ...]
        for lv, ld in left:
            for rv, rd in right:
                if ld + rd <= self.dist:
                    # 如果你想去重/统一顺序，可以用 tuple(sorted((lv, rv)))
                    self.res.append((lv, rv))

    def dfs(self, node: Optional['TreeNode']) -> List[Tuple[int, int]]:
        # return: list of (leafVal, distFromLeafToThisNode)
        if not node:
            return []

        # 叶子：离当前 node 的距离是 0，但为了让父节点看到它离父节点是 1，这里直接返回 dist=1（和 count 版本一致）
        if not node.left and not node.right:
            return [(node.val, 1)]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 在当前 node 结算跨左右子树的 pair
        self.merge_collect(left, right)

        # 往上返回：距离 +1，并剪枝
        up: List[Tuple[int, int]] = []
        for v, d in left + right:
            nd = d + 1
            if nd < self.dist:
                up.append((v, nd))
        return up

