# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #medium
    #linkedlist
    #time:On
    #space:O1
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        prev = None
        p0= dummy = ListNode(0, next = head)
        cur = head

        #recursively process k times:
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            #cur = 4,prev = 3
            nxt = p0.next
            nxt.next = cur
            p0.next = prev
            p0 = nxt

        return dummy.next

