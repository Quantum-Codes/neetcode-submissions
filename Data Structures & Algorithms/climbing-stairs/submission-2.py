class Solution:
    def climbStairs(self, n: int) -> int:
        one_back = 1
        two_back = 1

        for i in range(2, n+1):
            one_back, two_back = one_back+two_back, one_back
        return one_back