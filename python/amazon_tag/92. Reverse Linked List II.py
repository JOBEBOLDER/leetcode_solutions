# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #medium
    #time:On
    #space:O1
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        p0 = dummy

        #first move the left pointer to the left bound
        for _ in range(left - 1):
            p0 = p0.next

        #apply the reverse linkedlist method
        prev = None
        cur = p0.next

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        p0.next.next = cur
        p0.next = prev

        return dummy.next

        