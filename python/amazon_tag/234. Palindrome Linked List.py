# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # use a arr to store the val of the linkedlist
        val = []
        current_node = head

        while current_node is not None:
            val.append(current_node.val)
            current_node = current_node.next
        return val == val[::-1]#把数组倒过来，如果和原来数组一样

        #时间复杂度：O(n)，需要遍历一次链表
#空间复杂度：O(n)，需要额外的数组空间存储所有节点值