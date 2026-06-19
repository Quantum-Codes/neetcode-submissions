# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        visited.add(head)

        if head is None:
            return False

        while head.next:
            head = head.next
            if head in visited:
                return True
            
            visited.add(head)

        return False
