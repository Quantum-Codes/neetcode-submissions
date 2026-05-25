class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # max freq = len(nums). idx = freq for bucketsort list
        buckets = [[] for _ in range(len(nums)+1)]
        for item, f in freq.items():
            buckets[f].append(item)
        soln = []
        for i in range(len(buckets)-1, -1, -1):
            soln.extend(buckets[i])
        return soln[:k]