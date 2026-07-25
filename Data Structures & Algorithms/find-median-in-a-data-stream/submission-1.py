class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) == 1:
            return self.heap[0]

        heap = self.heap.copy()

        for _ in range(len(self.heap) // 2 - 1):
            heapq.heappop(heap)
    
        mid2  = heapq.heappop(heap)
        mid = heapq.heappop(heap)
        # 1 2 3 4
        if len(self.heap) & 1 == 1:
            return mid # n//2
        else:
            return (mid + mid2) / 2 # n//2 and n//2-1
        
