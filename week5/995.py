from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        starts = [0] * n
        flipped = 0
        ans = 0

        for i, bit in enumerate(nums):
            if i >= k:
                flipped ^= starts[i - k]

            if bit == flipped:
                if i + k > n:
                    return -1
                starts[i] = 1
                flipped ^= 1
                ans += 1

        return ans
