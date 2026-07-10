class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyStore = {}
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
         
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.keyStore:
            self.remove(self.keyStore[key])
            self.insert(self.keyStore[key])
            return self.keyStore[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyStore:
            self.remove(self.keyStore[key])
        node = Node(key, value)
        self.keyStore[key] = node
        self.insert(self.keyStore[key])

        if len(self.keyStore) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.keyStore[lru.key]

        
