# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        res = ListNode() # dummy head will be removed later
        cur_res = res

        while cur1 is not None or cur2 is not None:
            cur1_val = float('inf') if cur1 is None else cur1.val
            cur2_val = float('inf') if cur2 is None else cur2.val

            if cur1_val < cur2_val:
                new_node = ListNode(val = cur1_val)
                cur1 = cur1.next
            else:
                new_node = ListNode(val = cur2_val)
                cur2 = cur2.next

            cur_res.next = new_node
            cur_res = new_node
        
        return res.next
