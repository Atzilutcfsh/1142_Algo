from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right = -1
        max_seen = float("-inf")

        for i, num in enumerate(nums):
            if num < max_seen:
                right = i
            else:
                max_seen = num

        left = len(nums)
        min_seen = float("inf")

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        return 0 if right == -1 else right - left + 1
