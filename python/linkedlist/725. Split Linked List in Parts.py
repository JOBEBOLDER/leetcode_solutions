# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # to iterate the linkedlist and make it into a array
        #and get the lenght of the array devide by k
            #- if length/k the remainder not 0,then assign the extra part from the begining 
        # assign the k parts to result list
        #时间复杂度O(n + k)遍历链表O(n) + 处理k个部分O(k)空间复杂度O(k)result数组存储k个头节点引用

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        #get the length
        base_size = n // k
        extra_size = n % k

        result = []
        cur = head

        for i in range(k):
            part_size = base_size + (1 if i < extra_size else 0)

            part_head = cur
            result.append(part_head)

            # 如果当前部分不为空，需要找到这部分的尾节点并断开连接
            if cur:
                for j in range(part_size - 1):
                    cur = cur.next

                # 断开与后面链表的连接
                if cur:
                    next_part = cur.next
                    cur.next = None
                    cur = next_part

        return result


            




