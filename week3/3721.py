from typing import List

class SegTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.mn = [0] * (4 * self.n)
        self.mx = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)

    def build(self, idx: int, l: int, r: int, arr: List[int]) -> None:
        if l == r:
            self.mn[idx] = self.mx[idx] = arr[l]
            return
        m = (l + r) // 2
        self.build(idx * 2, l, m, arr)
        self.build(idx * 2 + 1, m + 1, r, arr)
        self.pull(idx)

    def pull(self, idx: int) -> None:
        self.mn[idx] = min(self.mn[idx * 2], self.mn[idx * 2 + 1])
        self.mx[idx] = max(self.mx[idx * 2], self.mx[idx * 2 + 1])

    def apply(self, idx: int, v: int) -> None:
        self.mn[idx] += v
        self.mx[idx] += v
        self.lazy[idx] += v

    def push(self, idx: int) -> None:
        if self.lazy[idx]:
            v = self.lazy[idx]
            self.apply(idx * 2, v)
            self.apply(idx * 2 + 1, v)
            self.lazy[idx] = 0

    def range_add(self, ql: int, qr: int, val: int) -> None:
        if ql > qr:
            return
        self._range_add(1, 0, self.n - 1, ql, qr, val)

    def _range_add(self, idx: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
        if ql <= l and r <= qr:
            self.apply(idx, val)
            return
        self.push(idx)
        m = (l + r) // 2
        if ql <= m:
            self._range_add(idx * 2, l, m, ql, qr, val)
        if qr > m:
            self._range_add(idx * 2 + 1, m + 1, r, ql, qr, val)
        self.pull(idx)

    def rightmost_zero_from(self, start: int) -> int:
        return self._rightmost_zero_from(1, 0, self.n - 1, start)

    def _rightmost_zero_from(self, idx: int, l: int, r: int, start: int) -> int:
        if r < start:
            return -1
        if self.mn[idx] > 0 or self.mx[idx] < 0:
            return -1
        if l == r:
            return l

        self.push(idx)
        m = (l + r) // 2

        res = self._rightmost_zero_from(idx * 2 + 1, m + 1, r, start)
        if res != -1:
            return res
        return self._rightmost_zero_from(idx * 2, l, m, start)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        # next_pos[i] = nums[i]下一次出現的位置
        next_pos = [n] * n
        last = {}
        for i in range(n - 1, -1, -1):
            if nums[i] in last:
                next_pos[i] = last[nums[i]]
            last[nums[i]] = i

        # base[r] = 當左端點 = 0 時，
        #           subarr [0..r] 的
        #           distinct odd - distinct even
        seen = set()
        cur = 0
        base = [0] * n
        for i, x in enumerate(nums):
            if x not in seen:
                seen.add(x)
                cur += 1 if x & 1 else -1
            base[i] = cur

        seg = SegTree(base)
        ans = 0

        for l in range(n):
            # 找最右邊的 r >= l s.t. balance = 0
            r = seg.rightmost_zero_from(l)
            if r != -1:
                ans = max(ans, r - l + 1)

            # 左端點往右移ㄉ時候, 對某段r整個區間加值
            if l + 1 < n:
                delta = -1 if nums[l] & 1 else 1
                seg.range_add(l, next_pos[l] - 1, delta)

        return ans