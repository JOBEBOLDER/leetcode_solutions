# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    intput: binary tree :root
    integer k:

    perfect binary tree:
    -left,right node number should be equal

    dfs:what should i return?
    what info should i need?
    -left node,right node number -> left subtree and right subtree number should be the same
    -root is perferect binary tree or not->should be determined by height
    -
	•	Time: O(n) ✅（每个节点访问一次）
	•	Space: O(h) ✅（递归栈，h 是树高）
	•	如果你额外存了 node_size 来排序：
	•	额外空间是 O(m)（m = perfect 子树的数量，最坏 O(n)）
	•	排序还会带来 O(m log m) 的时间
    
    '''
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        #base case 
        if not root:
            return -1
        
        self.node_size = []
        self.dfs(root)
         # ✅ 改：数量不够，返回 -1
        if len(self.node_size) < k:
            return -1
        self.node_size.sort(reverse = True)

        return self.node_size[k-1]


    def dfs(self,root):
        #base case
        if root is None:
            return [0,0]

        if root.left is None and root.right is None:
            self.node_size.append(1)
            return [1,1]

        left_height,left_size = self.dfs(root.left)
        right_height,right_size = self.dfs(root.right)

        height = max(left_height,right_height) + 1
        size = left_size + right_size + 1

        # ✅ 改：必须保证左右子树本身是 perfect（size != -1），且高度相同,同时其实不需要 left_size == right_size，只要高度相同且都 perfect 就行。
        if left_size != -1 and right_size != -1 and left_height == right_height and left_size == right_size:
            self.node_size.append(size)
            return [height, size]
        else:
            return [height, -1]


