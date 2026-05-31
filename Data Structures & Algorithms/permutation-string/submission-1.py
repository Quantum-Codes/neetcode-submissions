class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        if len(s1) > len(s2):
            return False
        left = 0
        s2_map = Counter(s2[:len(s1)])

        if s1_map == s2_map:
            return True

        for right in range(len(s1), len(s2)):
            s2_map[s2[left]] -= 1
            left += 1
            s2_map[s2[right]] += 1

            if s1_map == s2_map:
                return True
        
        return False
