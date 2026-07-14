# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Measure if k nodes exist
        # if len < k then leave it and just link to all prev, then stop
        # if len = k left then carefully reverse:
        #   detach from both ends
        #   reverse chunk
        #   reattach back
        #   might need to have a dummy on both ends to select start and end

        cur = head 
        solnhead = ListNode(next = head) # dummy infront of global list
        prevchunkend = solnhead
        while True:
            chunkhead = cur # save the head to reference later
            # now count if k items are present
            count = 1 # we are at head (Cur)
            while count < k and cur:
                cur = cur.next
                count += 1
            
            # exit if less nodes exist
            if count < k or not cur:
                break # it is already attached.
            
            # cur is at the last node.
            # point at the end to keep it.
            end = cur # pointer to end
            nextchunkhead = cur.next # save. might lose when reversing
            end.next = None # detach to isolate

            # we have isolated the chunk now. head and tail are disconnected
            # now can reverse normally
            prev = chunkhead
            cur = prev.next
            while cur:
                # save future nodes
                nextnode = cur.next
                # reverse link
                cur.next = prev
                # move ahead
                prev = cur
                cur = nextnode
            
            # now reattach
            # tail is new head pointer and head is new tailpointer
            prevchunkend.next = end
            chunkhead.next = nextchunkhead

            # reattached
            # now prepare for next loop
            prevchunkend = chunkhead
            cur = chunkhead.next

            
        return solnhead.next
