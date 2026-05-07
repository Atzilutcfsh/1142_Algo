from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -10**20
        candidates = deque()

        for x, y in points:
            while candidates and x - candidates[0][0] > k:
                candidates.popleft()

            if candidates:
                ans = max(ans, x + y + candidates[0][1])

            value = y - x
            while candidates and candidates[-1][1] <= value:
                candidates.pop()
            candidates.append((x, value))

        return ans
