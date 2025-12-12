# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    understand:
    input: linkedlist
    output:treenode
    questions:
    -empty,one
    -
        #determine the listnode length == even/odd->pick the root
            -do a for loop->get the length of the cur linklist
        #then we can just devide from there, []root[]

        how to balance?-> 
        mid = (l + r) // 2
	•	根节点值是 arr[mid]
    然后剩下的元素自动分成两段：
	•	左段 arr[l..mid-1] 必须全部 < root ⇒ 递归建左子树
	•	右段 arr[mid+1..r] 必须全部 > root ⇒ 递归建右子树
	•	Time: O(n)
	•	扫一遍链表转数组 O(n)
    	Space: O(n)
	•	主要是数组 arr 占 O(n)
  
    '''
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def build(l:int,r:int) -> Optional[TreeNode]:
            #dfs base case:
            if l > r:
                return None

            mid = (l+r) // 2
            #build the treeroot
            root = TreeNode(arr[mid])
            root.left = build(l,mid-1)
            root.right = build(mid + 1,r)
            return root

        return build(0,len(arr)-1)

