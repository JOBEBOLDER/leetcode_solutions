class Node:
    #basic ideas, using doubly linkedlist to mimic the library access book
    def __init__(self,key=0,val=0,prev = None,next=None):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_value = {}

    def get(self, key: int) -> int:
        node = self.get_helper(key)
        return node.val if node else -1

    def get_helper(self,key):
        if key not in self.key_to_value:
            return 
        #if exist:
        node = self.key_to_value[key]
        self.remove(node)
        self.push_front(node)

        return node

        
    def put(self, key: int, value: int) -> None:
        #two cases:
        #if node exist,update the value
        node = self.get_helper(key)
        if node:
            node.val = value
            return

        #otherwise: create new node and push front
        self.key_to_value[key] = node = Node(key,value)
        self.push_front(node)
        if len(self.key_to_value) > self.capacity:
            backnode = self.dummy.prev
            del self.key_to_value[backnode.key]
            self.remove(backnode)

    def push_front(self,x:Node):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

    def remove(self,x:Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)