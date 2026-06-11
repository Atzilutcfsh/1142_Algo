class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = 0
        best_right = 0

        def expand(left: int, right: int) -> None:
            nonlocal best_left, best_right

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1
            right -= 1

            if right - left > best_right - best_left:
                best_left = left
                best_right = right

        for center in range(len(s)):
            expand(center, center)
            expand(center, center + 1)

        return s[best_left : best_right + 1]
