class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter()
        s2_map = Counter()
        left = right = 0
        s1_len = len(s1)

        if len(s1) > len(s2):
            return False

        # construct s1_map
        for right in range(len(s1)):
            s1_map[s1[right]] += 1

            # also construct first window of s2
            s2_map[s2[right]] += 1

        if s1_map == s2_map:
            return True

        for right in range(right+1, len(s2)):
            s2_map[s2[left]] -= 1
            left += 1
            s2_map[s2[right]] += 1

            if s1_map == s2_map:
                return True
        
        return False
