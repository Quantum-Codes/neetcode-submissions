class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        array = self.store[key] # Not copying. O(1)
        left = 0
        right = len(array) - 1

        # 0 10 20 30 40 50 60 70 80 90
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= array[mid][0]:
                res = array[mid][1] # mid could be the answer
                left = mid + 1
            elif timestamp < array[mid][0]:
                right = mid - 1
            else:
                return array[mid][1]
        
        return res