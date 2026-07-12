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
        new_head = Node(0)
        new_cur = new_head # dummy exists rn
        new_list = []

        cur = head
        old_list = []

        # map out the old list
        while cur:
            old_list.append(cur)

            new_list.append(Node(cur.val)) # creating a new list without the random
            new_cur.next = new_list[-1]

            new_cur = new_cur.next
            cur = cur.next
        
        # O(n^2) approach. can try to use a dict here for O(n). But keys should be immutable and another problem is that vals can be duplicate
        # fill the old pointers
        for i in range(len(old_list)):
            new_list[i].random = None if old_list[i].random == None else new_list[old_list.index(old_list[i].random)]
        
        return new_head.next
        

        

        
