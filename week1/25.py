# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            i = 0
            kth = group_prev
            while i < k and kth:
                kth = kth.next
                i += 1
            if not kth:
                break

            group_next = kth.next
            
            curr = group_prev.next
            prev = group_next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            new_group_tail = group_prev.next
            group_prev.next = prev
            group_prev = new_group_tail


        return dummy.next
