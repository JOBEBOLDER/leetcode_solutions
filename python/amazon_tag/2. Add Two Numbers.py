# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #medium:
    #time:时间复杂度为 O(max(m,n))，
    #space:空间复杂度应该是 O(n)，其中 n 是较长链表的长度，因为需要创建一个新的链表来存储结果。
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        #create a extra listnode to initialize the result
        dummy = ListNode()#dummy is a node
        p = dummy#p is a pointer to keep track of the node

        carry = 0

        while p1 or p2 or carry:

            val = carry
            if p1:
                val += p1.val
                p1 = p1.next

            if p2:
                val += p2.val
                p2 = p2.next

            carry = val // 10 #calculate the ecimal number
            val  = val % 10 #calculate the single-digit

            p.next = ListNode(val)
            p = p.next

        return dummy.next

        
