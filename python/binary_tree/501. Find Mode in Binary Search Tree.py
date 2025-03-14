# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # this is a BST
    # we need to return all the modes

    # we can print all the values out, using inorder traversal, and then using Counter to calculate the frequency

    #time:On
    #space:On
    def __init__(self):
        self.res = [] # to store the result

    
    def traversal(self, root:Optional[TreeNode]):
        # base case
        if root is None:
            return None

        self.traversal(root.left)
        self.res.append(root.val)
        self.traversal(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        output = []
        count_dict = Counter(self.res)

        # find the max freq
        max_freq = max(count_dict.values())

        for num, freq in count_dict.items():
            if freq == max_freq:
                output.append(num)
        return output
                

        

        ''' # 使用 Counter 计算频率
        count_dict = Counter(self.res)
        
        # 找出最大频率
        max_freq = max(count_dict.values())
        
        # 返回所有具有最大频率的值
        return [num for num, freq in count_dict.items() if freq == max_freq]'''        

                


        