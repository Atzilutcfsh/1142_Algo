from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        jumps = {stone: set() for stone in stones}
        jumps[0].add(0)

        for stone in stones:
            for jump in jumps[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    next_stone = stone + next_jump

                    if next_jump <= 0 or next_stone not in jumps:
                        continue

                    if next_stone == target:
                        return True

                    jumps[next_stone].add(next_jump)

        return target == 0
