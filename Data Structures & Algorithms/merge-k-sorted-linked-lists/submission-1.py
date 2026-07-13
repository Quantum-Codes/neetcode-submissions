# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        select = 0

        while True:
            if select + 1 >= len(lists):
                return lists[select] if len(lists) > select else None

            head1 = lists[select]
            head2 = lists[select+1]
            head = ListNode()
            cur = head
            while head1 or head2:
                val1 = head1.val if head1 else float('inf')
                val2 = head2.val if head2 else float('inf')

                if val1 > val2:
                    cur.next = head2
                    head2 = head2.next
                else:
                    cur.next = head1
                    head1 = head1.next
                cur = cur.next
            
            lists.append(head.next)
            select += 2
