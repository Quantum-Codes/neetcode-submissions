class KthLargest:
    # only need to keep k largest numbers and return the lowest
    # can use priority queue and somehow track len
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(nums)
        for _ in range(len(self.heap) - k):
            heapq.heappop(self.heap)
        
        # now we have only k nums.

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
