import random
from typing import List


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)
        black = set(blacklist)
        self.mapping = {}
        last = n - 1

        for value in blacklist:
            if value >= self.bound:
                continue

            while last in black:
                last -= 1

            self.mapping[value] = last
            last -= 1

    def pick(self) -> int:
        value = random.randrange(self.bound)
        return self.mapping.get(value, value)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()