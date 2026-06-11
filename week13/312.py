from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        values = [1] + [num for num in nums if num > 0] + [1]
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for last in range(left + 1, right):
                    coins = (
                        dp[left][last]
                        + values[left] * values[last] * values[right]
                        + dp[last][right]
                    )
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]
