#你要设计一个linkedlist，总要包含listnode吧？如何design listnode呢：？
class ListNode:
    def __init__(self,val =0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    #medium
    def __init__(self):
        #initialize a dummy node
        self.dummy = ListNode()
        self.size = 0 #in order to check the boundry
        
        
    def get(self, index: int) -> int:
        #base case check:
        if index >= self.size or index < 0:
            return -1
        cur = self.dummy.next
        for i in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new = ListNode(val,self.dummy.next)
        self.dummy.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #这样无法在末尾添加节点。应该允许 index == self.size 的情况，修改为：
        if index < 0 or index > self.size:
            return 
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(val,cur.next)
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)