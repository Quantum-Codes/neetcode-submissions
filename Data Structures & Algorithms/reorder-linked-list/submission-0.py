# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque() #ignore head here.

        cur = head
        while cur.next:
            queue.append(cur.next)
            cur = cur.next
        
        # reorder
        i = 0
        list_reordered = head
        while queue:
            if i % 2 == 0:
                list_reordered.next = queue.pop()
            else:
                list_reordered.next = queue.popleft()
            i = 1 - i
            list_reordered = list_reordered.next
        
        list_reordered.next = None
        
