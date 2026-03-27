from typing import List

MOD = 10**9 + 7
NEG_INF = -10**21   

class Node:
    def __init__(self):
        # 因為 merge 左右區間時，要知道邊界有沒有撞到
        self.s00 = 0
        self.s01 = 0
        self.s10 = 0
        self.s11 = 0


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [Node() for _ in range(self.n * 4)]
        self.build(1, 0, self.n - 1, nums)

    def push_up(self, idx: int) -> None:
        left = self.tree[idx * 2]
        right = self.tree[idx * 2 + 1]
        cur = self.tree[idx]

        # 左不選、右不選
        cur.s00 = max(
            left.s00 + right.s00,
            left.s00 + right.s10,
            left.s01 + right.s00,
        )

        # 左不選、右選
        cur.s01 = max(
            left.s00 + right.s01,
            left.s00 + right.s11,
            left.s01 + right.s01,
        )

        # 左選、右不選
        cur.s10 = max(
            left.s10 + right.s00,
            left.s10 + right.s10,
            left.s11 + right.s00,
        )

        # 都選
        cur.s11 = max(
            left.s10 + right.s01,
            left.s10 + right.s11,
            left.s11 + right.s01,
        )

    def build(self, idx: int, l: int, r: int, nums: List[int]) -> None:
        if l == r:
            # 不選它 0
            # 選它 max(nums[l], 0)
            val = max(nums[l], 0)
            node = self.tree[idx]
            node.s00 = 0
            node.s01 = NEG_INF
            node.s10 = NEG_INF
            node.s11 = val
            return

        mid = (l + r) // 2
        self.build(idx * 2, l, mid, nums)
        self.build(idx * 2 + 1, mid + 1, r, nums)
        self.push_up(idx)

    def update(self, idx: int, l: int, r: int, pos: int, val: int) -> None:
        if l == r:
            # 單點更新reset
            node = self.tree[idx]
            node.s00 = 0
            node.s01 = NEG_INF
            node.s10 = NEG_INF
            node.s11 = max(val, 0)
            return

        mid = (l + r) // 2
        if pos <= mid:
            self.update(idx * 2, l, mid, pos, val)
        else:
            self.update(idx * 2 + 1, mid + 1, r, pos, val)

        # update 完往上 pull
        self.push_up(idx)

    def query(self) -> int:
        # root 就是整段 nums 的答案
        root = self.tree[1]
        return max(root.s00, root.s01, root.s10, root.s11)


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        st = SegmentTree(nums)
        ans = 0
        for pos, x in queries:
            # 改 nums[pos] = x
            st.update(1, 0, st.n - 1, pos, x)
            ans = (ans + st.query()) % MOD
        return ans