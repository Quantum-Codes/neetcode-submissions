# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        soln = ListNode(0)
        cur = soln

        # setup
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1
        
        while heap:
            cur.next = heapq.heappop(heap)[2]
            cur = cur.next
            # add the next node to heap
            if cur.next:
                heapq.heappush(heap, (cur.next.val, count, cur.next))
                count += 1

        return soln.next
        

        