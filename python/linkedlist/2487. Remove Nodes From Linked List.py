# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterate once , all the node in this linkedinlist, and store the result into a array
        # and then iterate from the back of the array,right to left
        # if we find out the left one is larger than the right one, pop it using stack
        #and the remaining elements in these stack, create a new linkedlist

        #t时间 O(n)，空间 O(n)。
        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next


        for i in range(len(stack) - 1):
            stack[i].next = stack[i+1]

        return stack[0] if stack else None