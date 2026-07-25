class MedianFinder:

    def __init__(self):
        self.leftheap = [] # maxheap
        self.rightheap = [] # minheap

    def addNum(self, num: int) -> None:
        # we maintain len(left) == len(right) or len(right) + 1
        
        # first find where this element needs to enter
        if not self.leftheap or self.leftheap[0] >= num:
            heapq.heappush_max(self.leftheap, num)
        else:
            heapq.heappush(self.rightheap, num)
        
        # now do the transfers
        if len(self.leftheap) < len(self.rightheap):
            heapq.heappush_max(self.leftheap, heapq.heappop(self.rightheap))
        elif len(self.leftheap) == len(self.rightheap) + 2:
            heapq.heappush(self.rightheap, heapq.heappop_max(self.leftheap))
        
        # this is O(logN)

    def findMedian(self) -> float:
        if (len(self.leftheap) + len(self.rightheap)) & 0b1: # true if odd
            return self.leftheap[0]
        else:
            return (self.leftheap[0] + self.rightheap[0]) / 2
             
        