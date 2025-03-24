# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #一般问子树问题都是后序遍历
    #medium,
    #time,space:ON^2
    def __init__(self):
        self.memo = {} #dic record the freq of the subtree
        self.res = [] #record the result

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res


    def traverse(self, root):
        #base case:
        if root is None:
            return "#"

        #postorder traverse:
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        subtree = left + "," + right + "," + str(root.val)
        
        freq = self.memo.get(subtree,0)

        #record the freq in postorder traversal
        if freq == 1:
            self.res.append(root)
        self.memo[subtree] = freq + 1

        return subtree     


'''
时间复杂度: O(n²)

我们需要遍历整棵树的所有 n 个节点，这是 O(n)
对于每个节点，我们构建序列化字符串 subtree，在最坏情况下，这个字符串的长度可能是 O(n)
字符串连接操作 (left + "," + right + "," + str(root.val)) 在最坏情况下也是 O(n)
因此总时间复杂度是 O(n²)

空间复杂度: O(n²)

哈希表 self.memo 存储所有子树的序列化字符串，有 n 个可能的子树
每个序列化字符串在最坏情况下长度为 O(n)
结果列表 self.res 最多存储 n 个节点引用
递归调用栈的深度为树的高度，最坏情况下是 O(n)
因此总空间复杂度是 O(n²)'''   