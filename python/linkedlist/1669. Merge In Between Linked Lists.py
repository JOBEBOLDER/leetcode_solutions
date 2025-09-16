# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #my plan is to traverse to the prev a node, and connect this node to b+1 node
        #base case:
        dummy = ListNode(0,list1)

        # find the "part that we need to cut,the left most point"
        prev_a = dummy
        for _ in range(a):
            prev_a = prev_a.next

         # find the "part that we need to cut,the right most point"
        prev_b = prev_a
        for _ in range(b - a + 1):
            prev_b = prev_b.next


        # connect list2:
        tail = list2
        while tail.next:
            tail = tail.next

        prev_a.next = list2
        tail.next = prev_b.next


        return dummy.next





        



