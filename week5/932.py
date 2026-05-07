from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]

        while len(ans) < n:
            odds = [2 * x - 1 for x in ans if 2 * x - 1 <= n]
            evens = [2 * x for x in ans if 2 * x <= n]
            ans = odds + evens

        return ans
