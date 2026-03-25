class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        left = arr[:mid][::-1]
        right = arr[mid:][::-1]
        nums[::2] = left
        nums[1::2] = right