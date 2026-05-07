from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        position = {person: i for i, person in enumerate(row)}
        swaps = 0

        for i in range(0, len(row), 2):
            first = row[i]
            partner = first ^ 1

            if row[i + 1] == partner:
                continue

            partner_index = position[partner]
            other = row[i + 1]

            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            position[partner] = i + 1
            position[other] = partner_index
            swaps += 1

        return swaps
