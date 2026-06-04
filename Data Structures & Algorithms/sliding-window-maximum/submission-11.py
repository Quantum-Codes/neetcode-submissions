class Solution:
    # O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        soln = []

        for i in range(len(nums)):            
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            # remove expired elements from front
            while len(window) > 1 and window[0] < i - k + 1:
                window.popleft()
            
            soln.append(nums[window[0]])
        
        return soln[k-1:] # first k-1 is wrong cuz till then we didnt construct the first window