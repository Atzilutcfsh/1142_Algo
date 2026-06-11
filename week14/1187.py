from bisect import bisect_right
from math import inf
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        replacements = sorted(set(arr2))
        dp = {-1: 0}

        for value in arr1:
            next_dp = {}

            for previous, operations in dp.items():
                if value > previous:
                    next_dp[value] = min(next_dp.get(value, inf), operations)

                index = bisect_right(replacements, previous)
                if index < len(replacements):
                    replacement = replacements[index]
                    next_dp[replacement] = min(
                        next_dp.get(replacement, inf),
                        operations + 1,
                    )

            if not next_dp:
                return -1

            dp = next_dp

        return min(dp.values())
