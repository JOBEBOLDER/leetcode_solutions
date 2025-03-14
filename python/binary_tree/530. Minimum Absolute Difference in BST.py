# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #时间复杂度：O(n)，而不是O(2n)。虽然你有一次遍历来构建数组，然后再遍历一次数组来找最小差值，但这仍然是O(n)。常数因子2在大O表示法中被省略。
    #空间复杂度：O(n)，因为你创建了一个数组来存储所有节点值。
    # BST inorder traversal is increasing order
    #思路：用一个数组储存所有node的value，然后再循环一遍比较更新min——value
    def __init__(self):
        self.res = []
        #应该初始化为一个足够大的数（比如 float('inf')）
        self.result = float('inf')

    def traversal(self, root:Optional[TreeNode]):
        if root is None:
            return 

        self.traversal(root.left)
        self.res.append(root.val)
        self.traversal(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = []
        self.traversal(root)
        
        
        for i in range(1,len(self.res)):
            self.result = min(self.result, self.res[i] - self.res[i - 1])

        return self.result
