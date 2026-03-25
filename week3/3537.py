from typing import List

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[0]]

        small = self.specialGrid(n - 1)
        m = len(small)
        block = m * m

        ans = [[0] * (2 * m) for _ in range(2 * m)]

        for i in range(m):
            for j in range(m):
                ans[i][j] = small[i][j] + 3 * block
                ans[i][j + m] = small[i][j]
                ans[i + m][j] = small[i][j] + 2 * block
                ans[i + m][j + m] = small[i][j] + block

        return ans