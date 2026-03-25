from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        #init
        n = len(nums)
        if n <= 1:
            return 0
        
        val = nums[:]
        alive = [True] * n
        leftindex = [-1]*n
        rightindex = [-1]*n
        for i in range(n):
            leftindex[i] = i-1
            rightindex[i] = i+1
        leftindex[0] = -1
        rightindex[n-1] = -1

        #decrease檢查器
        def is_decreasing(i:int,j:int)-> int:
            if i == -1 or j ==-1 : return 0
            if val[i] > val[j]: return 1 
            else : return 0
        #生存確認
        def is_alive_pair(s:int,i:int,j:int)-> bool:
            return alive[i] and alive[j] and rightindex[i] == j and s == val[i] + val[j]

        decreasing_count = 0
        for i in range(n-1):
            decreasing_count += is_decreasing(i,i+1)

        heap = []
        # heap item: (pair_sum, left_index, right_index)
        for i in range(n-1):
            heappush(heap,(val[i]+val[i+1],i,i+1))
        
        ans = 0

        #until nondecreasing
        while decreasing_count > 0 :
            while True:
                s,i,j = heappop(heap)
                if is_alive_pair(s,i,j):
                    break

            L = leftindex[i]
            R = rightindex[j]
            
            decreasing_count -= is_decreasing(L,i)
            decreasing_count -= is_decreasing(i,j)
            decreasing_count -= is_decreasing(j,R)
            
            val [i] += val [j]
            alive[j] = False

            rightindex[i] = R
            if R != -1 : leftindex[R] = i

            decreasing_count += is_decreasing(L,i)
            decreasing_count += is_decreasing(i,R)

            if L != -1: heappush(heap, ( val[L]+val[i] , L, i))
            if R != -1: heappush(heap, ( val[i]+val[R] , i, R))

            ans += 1
        
        return ans