# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time:On
    #space:空间复杂度：O(1)，而不是 O(n)。虽然你创建了两个新的链表头节点（dummy1 和 dummy2），但你并没有创建任何新的节点来复制原链表中的节点，而是直接重新组织了原链表中的节点。因此，额外空间复杂度是常数级别的。
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)

        p = head
        p1 = dummy1
        p2 = dummy2

        while p:
            if p.val >= x: #don't forget the equal to x
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next

            temp = p.next
            # 断开原链表中的每个节点的 next 指针
            p.next = None
            p = temp

        p1.next = dummy2.next

        return dummy1.next
'''while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else :
                p1.next = p
                p1 = p1.next
            temp = p.next
            p.next = None
            p = temp

        p1.next = dummy2.next
        return dummy1.next'''

