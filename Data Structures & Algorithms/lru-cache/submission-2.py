class Node:
    def __init__(self, key=0, val=0, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.nodes = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if not node:
            return -1
        if node is not self.head.next: #check if alr in pos
            # extract from current pos
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            
            # make new head
            node.prev = self.head
            node.next = self.head.next
            # stitch back into list
            self.head.next.prev = node
            self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.nodes.get(key):
            self.nodes[key].val = value
            self.get(key)
            return 

        if len(self.nodes) >= self.capacity:
            node = self.tail.prev
            del self.nodes[node.key]
            # extract node from list
            node.prev.next = self.tail
            self.tail.prev = node.prev
        
        self.nodes[key] = Node(key=key, val=value, prev=self.head, next = self.head.next)
        self.head.next.prev = self.nodes[key]
        self.head.next = self.nodes[key]

