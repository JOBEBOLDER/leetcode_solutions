# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    #time:On
    #space:O1

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #base case:
        if root is None:
            return 

        #to find the key
        #if the key is found:
        if key == root.val:
            #case1,left is None and right is not,return right directly
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right != None:
                return root.right
            elif root.right is None and root.left != None:
                return root.left
            else:
                cur = root.right
                #先找出root.right the smallest, then move the root.left to the new subtree看代码随想录450讲解
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
            #When we return root, we're essentially saying "I've made the necessary deletion in my right subtree, and now I'm returning myself with that updated right subtree to my parent."'''

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
            return root
