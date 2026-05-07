class Solution:
    def partitionString(self, s: str) -> int:
        parts = 1
        seen = set()

        for ch in s:
            if ch in seen:
                parts += 1
                seen.clear()
            seen.add(ch)

        return parts
