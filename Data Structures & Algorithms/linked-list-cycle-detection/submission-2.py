# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slowhead = head
        i = 0
        while head.next:
            head = head.next
            if i % 2 == 1:
                slowhead = slowhead.next # guaranteed to exist since head has walked
            i = 1 - i

            if head == slowhead:
                return True

        return False
