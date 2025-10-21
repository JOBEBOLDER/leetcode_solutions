# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #my ideas:
    #two scenarios:
    #left subtree: 1.only root:root is empty 2. has left child,left-> boundry, 3.no left, only right, then right node is the boundry node
    #if both has left and right, then their ultimate leaves are boundry
    #right subtree:
    #if only one subtree, return that node as a boundry node, otherwise: two subtree,return leaves as boundry
    '''
    题目要我们返回二叉树的边界（boundary），它包含四部分：
	1.	根节点（root）
	2.	左边界（left boundary，排除叶子节点）
	3.	所有叶子节点（leaves，从左到右）
	4.	右边界（right boundary，排除叶子节点，倒序加入）

最终顺序是：

root → left boundary → leaves → reversed(right boundary)

why two functions:?
我们需要两个（甚至三个小函数）是为了让逻辑清晰、职责单一：
	•	一个函数负责“找边界”（比如左边界、右边界）
	•	一个函数负责“找叶子”

    '''

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # base case:
        if not root:
            return []

        # we need 2 functions to traverse:
        def is_leave(node):
            #dfs end condition
            return not node.left and not node.right
        
        # start with left:
        res = [root.val]
        cur = root.left
        while cur:
            if not is_leave(cur):
                res.append(cur.val)

            if cur.left:
                cur = cur.left
            else:
                cur = cur.right

        def add_leaves(node):
            #dfs end condition:
            if not node:
                return 
            if is_leave(node):
                if node!= root: #in case , only one root node
                    res.append(node.val)
            else:
                add_leaves(node.left)
                add_leaves(node.right)

        add_leaves(root)

        #right boundry:右边界：一路往右走（不包括叶子），最后反转
        stack = []
        cur = root.right
        while cur:
            if not is_leave(cur):
                stack.append(cur.val)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        res.extend(reversed(stack))

        return res


