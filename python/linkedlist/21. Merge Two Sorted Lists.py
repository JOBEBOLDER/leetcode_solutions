# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #处理空链表：
        # 处理空链表的情况
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2

        dummy = ListNode()

        p = dummy

        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next

            else:
                p.next = p1
                p1 = p1.next
            p = p.next

## 不需要循环，直接连接剩余部分即可,because alreayd sorted

        if p1:
            p.next = p1
            p = p.next
        
        if p2:
            p.next = p2
            p = p.next

        return dummy.next
