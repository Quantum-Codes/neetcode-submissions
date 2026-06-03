from _heapq import heapify
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]

        # first window:
        nums = [-item for item in nums] # to make minheap to maxheap
        window = nums[:k]
        heapq.heapify(window)
        
        soln = [-window[0]]
        deleted = defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(window, nums[i])
            deleted[nums[i-k]] += 1
            popped = window[0]
            while deleted[popped] > 0:
                deleted[popped] -= 1
                heapq.heappop(window) # popped current max that we deleted
                popped = window[0] # peek next max to see if its deleted

            soln.append(-popped)
            
        return soln

