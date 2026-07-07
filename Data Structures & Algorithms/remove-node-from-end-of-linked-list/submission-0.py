# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        solnhead = ListNode()
        solnhead.next = head
        cur = solnhead
        # now we walk back to len - nth index. stand on the node right behind it
        for _ in range(length - n):
            cur = cur.next
        
        cur.next = cur.next.next if n != 1 else None # 1 skip. the only problem when deleting the last node. else node.next always exist. so do the ternary
        return solnhead.next