# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #medium
        # linkedlist ,two pointers:

        #time:On,space: O1

        dummy = ListNode()
        dummy.next = head

        current = dummy

        #base case :n = size of the node:
        size = 0
        count = head
        while count:
            size += 1
            count = count.next
        
        if size == n:
            return head.next

        for i in range(size - n):#3->2
            current = current.next
        current.next = current.next.next

        return dummy.next

