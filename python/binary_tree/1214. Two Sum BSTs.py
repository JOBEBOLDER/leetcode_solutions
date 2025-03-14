# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        #base case:
        if not root1 or not root2:
            return False

        #get the values list from the inorder1
        values1 = []
        self.inorder(root1, values1)

        values2 = []
        self.inorder(root2, values2)

        for val in values1:
            to_find = target - val
            if to_find in values2:
                return True
        return False


    def inorder(self, root:Optional[TreeNode],values:List[int]):
        if root is None:
            return

        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right,values)


        class Solution:
    '''
时间复杂度: O(n)

对两棵树进行中序遍历需要 O(n1 + n2) 时间，其中 n1 和 n2 分别是两棵树的节点数
遍历 values1 数组并检查每个元素的补数是否在 values2 中需要 O(n1) 次操作
在 Python 中，if to_find in values2 操作的平均时间复杂度是 O(1)（因为它将 values2 视为哈希集）
总体时间复杂度为 O(n1 + n2 + n1) = O(n)，其中 n = n1 + n2

空间复杂度: O(n)

存储两棵树的所有节点值需要 O(n1 + n2) = O(n) 的空间
递归调用栈在最坏情况下需要 O(h) 的空间，其中 h 是树的高度
总体空间复杂度为 O(n)'''