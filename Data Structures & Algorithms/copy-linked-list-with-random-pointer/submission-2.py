"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        new_list = []
        new_head = Node(0)
        new_cur = new_head
        old_indexes = {}
        old_list = []

        # first clone the linkedlist
        cur = head
        i = 0
        while cur:
            old_indexes[cur] = i
            new_list.append(Node(cur.val))
            new_cur.next = new_list[-1]
            old_list.append(cur)
            
            new_cur = new_cur.next
            cur = cur.next
            i += 1
        
        # map out the random pointers
        for i, node in enumerate(old_list):
            new_list[i].random = new_list[old_indexes[node.random]] if node.random is not None else None

        
        return new_head.next