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

        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur_res.next = cur1
                cur1 = cur1.next
            else:
                cur_res.next = cur2
                cur2 = cur2.next

            cur_res = cur_res.next

        cur_res.next = cur1 or cur2
        return res.next
