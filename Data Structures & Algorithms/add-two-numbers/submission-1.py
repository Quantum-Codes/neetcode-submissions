# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        cur1 = l1
        cur2 = l2

        carry = 0
        while cur1 or cur2 or carry:
            val1 = 0 if cur1 is None else cur1.val
            val2 = 0 if cur2 is None else cur2.val

            cur.next = ListNode((val1+val2+carry)%10)
            cur = cur.next
            carry = (val1+val2+carry)//10

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        

        
        return head.next