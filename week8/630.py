import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        total_time = 0
        taken = []

        for duration, last_day in sorted(courses, key=lambda course: course[1]):
            total_time += duration
            heapq.heappush(taken, -duration)

            if total_time > last_day:
                total_time += heapq.heappop(taken)

        return len(taken)
