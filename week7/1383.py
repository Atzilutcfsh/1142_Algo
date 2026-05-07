import heapq
from typing import List


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        mod = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        speed_sum = 0
        best = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            speed_sum += spd

            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)

            best = max(best, speed_sum * eff)

        return best % mod
