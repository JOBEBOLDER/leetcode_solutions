# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time:On
    #space:O1
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initialization
        dummy = ListNode()
        dummy.next = head

        current = dummy

        #讨论奇数和偶数的情况
        while current.next and current.next.next:
            #清楚记得步骤图，步骤123之后链表拉平
            #store the head as a temp:
            tmp = current.next
            tmp2 = current.next.next.next

            #begin to swap:
            current.next = current.next.next
            current.next.next = tmp
            tmp.next = tmp2

            #move the current node:
            current = current.next.next

        return dummy.next