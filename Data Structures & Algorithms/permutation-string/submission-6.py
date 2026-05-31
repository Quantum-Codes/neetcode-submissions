import string

class Solution:
    # O(26n). see next soln for O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = Counter(s2[:len(s1) - 1])  # one short
        matches = 0
        # prefill matches. if matches == 26 then s1_map == s2_map. O(1) check rather than O(26)
        for char in string.ascii_lowercase:
            if s1_map[char] == s2_map[char]:
                matches += 1

        for right in range(len(s1) - 1, len(s2)):
            if s2_map[s2[right]] == s1_map[s2[right]]: # if was matching before, then it wont now after dict increment
                matches -= 1
            s2_map[s2[right]] += 1 # complete the window
            if s2_map[s2[right]] == s1_map[s2[right]]: # if is matching now, increment
                matches += 1
            if matches == 26:
                return True
            if s2_map[s2[right - len(s1) + 1]] == s1_map[s2[right - len(s1) + 1]]:
                matches -= 1
            s2_map[s2[right - len(s1) + 1]] -= 1  # remove leftmost for next iteration
            if s2_map[s2[right - len(s1) + 1]] == s1_map[s2[right - len(s1) + 1]]:
                matches += 1

        return False