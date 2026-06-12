import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hours = lambda arr, k: sum([math.ceil(item / k) for item in arr])

        left = 1
        right = max(piles)
        hrs = 0
        while left <= right:
            k = (left + right) // 2
            hrs = hours(piles, k)

            if hrs > h:
                left = k + 1
            else:
                right = k - 1
        
        return int(left)


        # 0 1 2 (3) 4 5 6 7 8 9