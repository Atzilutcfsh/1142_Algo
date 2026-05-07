from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacements = 0
        limit = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= limit:
                limit = nums[i]
                continue

            parts = (nums[i] + limit - 1) // limit
            replacements += parts - 1
            limit = nums[i] // parts

        return replacements
