from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()
        heap = [(0, float("inf"))]
        ans = []

        for x, neg_height, right in events:
            if neg_height < 0:
                heapq.heappush(heap, (neg_height, right))

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            height = -heap[0][0]
            if not ans or ans[-1][1] != height:
                ans.append([x, height])

        return ans
