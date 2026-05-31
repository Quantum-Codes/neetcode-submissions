class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        s2_map = Counter(s2[:len(s1)])

        while right < len(s2)+1:
            if s1_map == s2_map:
                return True

            if right != len(s2):
                s2_map[s2[left]] -= 1
                left += 1
                s2_map[s2[right]] += 1
            right += 1
        
        return False
