class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: (x[0]**2 + x[1]**2)**0.5
        heap = []

        for point in points:
            heapq.heappush_max(heap, (dist(point), point))
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        return [item[1] for item in heap]