import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 把每條 list 的頭放進 heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while heap:
            # 取min
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            # exist .next -> heappush
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next