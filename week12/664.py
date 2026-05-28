class Solution:
    def strangePrinter(self, s: str) -> int:
        chars = []
        for ch in s:
            if not chars or chars[-1] != ch:
                chars.append(ch)

        s = "".join(chars)
        n = len(s)

        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            dp[left][left] = 1

            for right in range(left + 1, n):
                dp[left][right] = dp[left + 1][right] + 1

                for same in range(left + 1, right + 1):
                    if s[same] == s[left]:
                        middle = dp[left + 1][same - 1] if same > left + 1 else 0
                        dp[left][right] = min(
                            dp[left][right],
                            middle + dp[same][right],
                        )

        return dp[0][n - 1]
