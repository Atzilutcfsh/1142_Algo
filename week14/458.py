class Solution:
    def poorPigs(
        self,
        buckets: int,
        minutesToDie: int,
        minutesToTest: int,
    ) -> int:
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        capacity = 1

        while capacity < buckets:
            pigs += 1
            capacity *= states

        return pigs
