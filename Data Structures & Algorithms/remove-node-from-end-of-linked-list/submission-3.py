# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        solnhead = ListNode(0, head)
        slow = solnhead
        fast = solnhead

        for _ in range(n): # we make a gap of n - 1 when it had to be n-2. we are 1 back so we can delete the nth node
            fast = fast.next # number of nodes more than n

        while fast.next:
            fast = fast.next
            slow = slow.next # maintain gap until end
        
        # after loop, slow is at target
        slow.next = slow.next.next
        return solnhead.next