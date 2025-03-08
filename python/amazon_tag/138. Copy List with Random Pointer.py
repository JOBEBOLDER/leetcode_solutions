"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#对于数据结构复制，甭管他怎么变，你就记住最简单的方式：一个哈希表 + 两次遍历。
'''时间复杂度：O(n)

需要遍历链表两次，每次是O(n)
哈希表的查找和插入是O(1)的操作


空间复杂度：O(n)

需要一个哈希表来存储n个节点的映射'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originToClone = {}

        #the first traverse:
        p = head

        while p:
            if p not in originToClone:
                originToClone[p] = Node(p.val)
            p = p.next

        #second traverse:
        p = head

        while p:
            if p.next:
                originToClone[p].next = originToClone[p.next] #原来的node.next赋值给新node的下一个
            if p.random:
                originToClone[p].random = originToClone[p.random]

            p = p.next

        return originToClone.get(head)