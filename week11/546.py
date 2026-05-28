from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(left: int, right: int, same: int) -> int:
            if left > right:
                return 0

            while left < right and boxes[right] == boxes[right - 1]:
                right -= 1
                same += 1

            best = dp(left, right - 1, 0) + (same + 1) * (same + 1)

            for mid in range(left, right):
                if boxes[mid] == boxes[right]:
                    best = max(
                        best,
                        dp(left, mid, same + 1) + dp(mid + 1, right - 1, 0),
                    )

            return best

        return dp(0, len(boxes) - 1, 0)
