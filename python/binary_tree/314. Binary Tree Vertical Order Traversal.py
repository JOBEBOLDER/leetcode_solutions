# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:Time Complexity: O(NlogN) 
    #space:Space Complexity: O(N) where N is the number of nodes in the tree.

#First of all, we use a hash table to group the nodes with the same column index. The hash table consists of keys and values. In any case, the values would consume O(N) memory. 
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #solution:use a diction to store the value and the node,so we can keep track of the processing result
        # 创建一个默认字典，键是列号，值是节点值列表

        node_table = defaultdict(list)

        # 使用队列进行BFS，每个元素是(节点, 列号)
        queue = deque([(root,0)])

        while queue:
            node, col = queue.popleft()

            #append the node value according to the responding value to the col
            if node is not None:
                node_table[col].append(node.val)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [node_table[x] for x in sorted(node_table.keys())]