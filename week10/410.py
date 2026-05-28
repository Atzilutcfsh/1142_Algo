from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def can_split(limit: int) -> bool:
            pieces = 1
            current = 0

            for num in nums:
                if current + num > limit:
                    pieces += 1
                    current = num

                    if pieces > k:
                        return False
                else:
                    current += num

            return True

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
