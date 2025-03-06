class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    #mediun
    #hashmap,dict()
    #doubly linkedlist


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()
    
    def get_helper(self, key:int) ->Optional[Node]:
        #如果没有这本书
        if key not in self.key_to_node:  # 没有这本书
            return None

        #如果有这本书
        node = self.key_to_node[key]
        self.remove(node)# 把这本书抽出来
        self.push_front(node)
        return node

        #把这本书抽出来
        #放在最上面
        

    def get(self, key: int) -> int:
        node = self.get_helper(key) 
        return node.value if node else -1


    def put(self, key: int, value: int) -> None:
        node = self.get_helper(key)
        #如果有这本书，update这个value
        if node:
            node.value = value
            return
        #如果没有这本书：
        #创建新书
        #先创建一个node，然后把这个node存储到node dict
        self.key_to_node[key] = node = Node(key,value)

        self.push_front(node)#放在最上面

        #检查cap：
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书



    #doubly linkedlist helper function:
    def remove(self,x:Node)->None:
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x:Node)-> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)