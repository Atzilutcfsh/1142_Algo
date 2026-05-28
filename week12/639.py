class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7

        def single_count(ch: str) -> int:
            if ch == "*":
                return 9
            if ch == "0":
                return 0
            return 1

        def pair_count(first: str, second: str) -> int:
            if first == "*" and second == "*":
                return 15
            if first == "*":
                return 2 if "0" <= second <= "6" else 1
            if second == "*":
                if first == "1":
                    return 9
                if first == "2":
                    return 6
                return 0

            value = int(first + second)
            return 1 if 10 <= value <= 26 else 0

        prev_two = 1
        prev_one = single_count(s[0])

        for i in range(1, len(s)):
            current = (
                single_count(s[i]) * prev_one
                + pair_count(s[i - 1], s[i]) * prev_two
            ) % mod
            prev_two, prev_one = prev_one, current

        return prev_one
