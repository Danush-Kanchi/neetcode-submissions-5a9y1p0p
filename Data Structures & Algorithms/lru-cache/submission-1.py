class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        pre=self.right.prev
        nxt=self.right

        node.next=nxt
        nxt.prev=node

        node.prev=pre
        pre.next=node
    
    
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove(node)
            self.insert(node)
            return
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru=self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        
